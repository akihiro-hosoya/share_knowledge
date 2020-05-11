from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import ProfileForm, SignupUserForm
from allauth.account import views

# Create your views here.
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        # CustomUserクラスからログイン中のユーザー情報を取得
        user_data = CustomUser.objects.get(id=request.user.id)

        return render(request, 'accounts/profile.html',{
            'user_data': user_data,
        })

class ProfileEditView(View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        # テンプレートでフォームを表示したいので、ProfileFormクラスを呼び出し
        form = ProfileForm(
            request.POST or None,
            # フォームに初期値を与えるために、initialにデータベースの情報を設定
            initial={
                'first_name': user_data.first_name,
                'last_name': user_data.last_name,
                'department': user_data.department,
                'position': user_data.position,
            }
        )

        return render(request, 'accounts/profile_edit.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        # フォームに入力された値にエラーがないかをバリデートするメソッド
        if form.is_valid():
            user_data = CustomUser.objects.get(id=request.user.id)
            # バリデート後のデータを型に応じて一定のやり方で整形して返します
            user_data.first_name = form.cleaned_data['first_name'] # first_nameの項目に日付を文字列で入れたときに、常にuser_name.first_nameオブジェクトにしてくれます
            user_data.last_name = form.cleaned_data['last_name']
            user_data.department = form.cleaned_data['department']
            user_data.position = form.cleaned_data['position']
            # save関数をコールすることで保存
            user_data.save()
            return redirect('profile')

        return render(request, 'accounts/profile.html', {
            'form': form
        })

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            # self.logout()でログアウトする
            self.logout()
        return redirect('/')

class SignupView(views.SignupView):
    template_name = 'account/signup.html'
    form_class = SignupUserForm