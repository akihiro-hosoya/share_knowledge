from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    # 管理画面のユーザー変更フォーム(Form)とユーザー追加フォーム(Form)を自分で生成したフォーム(Form)で設定
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'affiliation', 'position', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields':('username','email','password')}),
        ('Personal info', {'fields': ('affiliation','position',)}),
        ('Permissions',{'fields':('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'affiliation', 'position', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# 登録
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)