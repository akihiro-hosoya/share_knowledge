from .models import Camera, Printer

def common(request):
    context = {
        'camera_list': Camera.objects.all(),
        'printer_list': Printer.objects.all(),
    }
    return context