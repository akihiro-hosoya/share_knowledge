from django import forms
from .models import Post, Comment, GrandCategory, ParentCategory, Category

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
