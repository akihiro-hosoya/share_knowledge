from .models import Category, ParentCategory, GrandCategory

def common(request):
    context = {
        'grand_list': GrandCategory.objects.all(),
        'parent_list': ParentCategory.objects.all(),
        'category_list': Category.objects.all(),
    }
    return context