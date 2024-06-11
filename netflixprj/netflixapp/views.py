from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . models import Profile, Movie


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    

