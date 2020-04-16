from .models import Camera

def common(request):
    context = {
        'canon_list': Camera.objects.all(),
        'sony_list': Camera.objects.all(),
        'olympus_list': Camera.objects.all(),
        'nikon_list': Camera.objects.all(),
    }
    return context