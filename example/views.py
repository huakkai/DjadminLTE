from django.contrib.auth import authenticate, login as django_login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


def index(request):
    context = {
        'site': 'Hello World.'
    }
    return render(request, 'example/index.html', context=context)


class LoginView(View):
    """
    login
    """
    def get(self, request):
        context = {
            'site': 'Hello World.'
        }
        return render(request, 'example/login.html', context=context)

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return HttpResponseRedirect('/e/index/')
            else:
                context = {'message': 'user not active'}
                return render(request, 'example/login.html', context=context)
        else:
            context = {'message': 'not user'}
            return render(request, 'example/login.html', context=context)

