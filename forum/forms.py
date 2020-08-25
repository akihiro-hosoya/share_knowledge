from django import forms
from forum.models import Post, Comment, GrandCategory, ParentCategory, Category
from accounts.models import CustomUser
# from django.conf import settings
# from django.core.mail import BadHeaderError, send_mail
# from django.http import HttpResponse


# class PostForm(forms.ModelForm):
#     grand_category = forms.ModelChoiceField(
#         label='大カテゴリー',
#         queryset=GrandCategory.objects,
#         required=False
#     )
#     parent_category = forms.ModelChoiceField(
#         label='中カテゴリー',
#         queryset=ParentCategory.objects,
#         required=False
#     )
#     class Meta:
#         model = Post
#         fields = ('author', 'grand_category', 'parent_category', 'category', 'title', 'text')

#     field_order = ('title', 'author', 'grand_category', 'parent_category', 'category', 'text')

class PostForm(forms.Form):
    # grandcategory_data = GrandCategory.objects.all()
    # grandcategory_choice = {}
    # for grandcategory in grandcategory_data:
    #     grandcategory_choice[grandcategory] = grandcategory
    # parentcategory_data = ParentCategory.objects.all()
    # parentcategory_choice = {}
    # for parentcategory in parentcategory_data:
    #     parentcategory_choice[parentcategory] = parentcategory
    category_data = Category.objects.all()
    category_choice = {}
    for category in category_data:
        category_choice[category] = category

    title = forms.CharField(max_length=50, label='タイトル')
    text = forms.CharField(label='内容', widget=forms.Textarea())
    # grandcategory = forms.ChoiceField(label='大カテゴリ', widget=forms.Select, choices=list(grandcategory_choice.items()))
    # parentcategory = forms.ChoiceField(label='中カテゴリ', widget=forms.Select, choices=list(parentcategory_choice.items()))
    category = forms.ChoiceField(label='小カテゴリ', widget=forms.Select, choices=list(category_choice.items()))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

class ContactForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=100)
    sender = forms.EmailField(label='Email', help_text='※ご確認の上、正しく入力してください。')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    myself = forms.BooleanField(label='同じ内容を受け取る', required=False)