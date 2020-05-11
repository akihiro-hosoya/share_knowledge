from .models import Category, ParentCategory, GrandCategory, Post, Comment, NewsPost

def common(request):
    context = {
        'grand_list': GrandCategory.objects.all(),
        'parent_list': ParentCategory.objects.all(),
        'category_list': Category.objects.all(),
        'grandCategory_list': GrandCategory.objects.all(),
        'parentCategory_list': ParentCategory.objects.all(),
        'news_list': NewsPost.objects.order_by('-published_date')[:3],
    }
    return context

