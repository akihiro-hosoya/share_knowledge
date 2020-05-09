from django.views import View
from django.shortcuts import render, redirect

# Create your views here.
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/profile.html')