from django import forms
from forum.models import Post, Comment, GrandCategory, ParentCategory, Category
from accounts.models import CustomUser
# from django.conf import settings
# from django.core.mail import BadHeaderError, send_mail
# from django.http import HttpResponse


class PostForm(forms.ModelForm):
    grand_category = forms.ModelChoiceField(
        label='大カテゴリー',
        queryset=GrandCategory.objects,
        required=False
    )
    parent_category = forms.ModelChoiceField(
        label='中カテゴリー',
        queryset=ParentCategory.objects,
        required=False
    )
    class Meta:
        model = Post
        fields = ('author', 'grand_category', 'parent_category', 'category', 'title', 'text')

    field_order = ('title', 'author', 'grand_category', 'parent_category', 'category', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

class ContactForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=100)
    sender = forms.EmailField(label='Email', help_text='※ご確認の上、正しく入力してください。')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    myself = forms.BooleanField(label='同じ内容を受け取る', required=False)