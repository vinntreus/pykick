from django.shortcuts import render
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from candidate.models import get_candidates


def home(request):
    context = {
        'candidates': get_candidates()
    }
    return render(request, 'startpage.html', context)


def login(request):
    if request.method == 'GET':
        context = {
            'logged_in': request.user.is_authenticated
        }
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
        else:
            messages.error(request, 'Wrong username or password')

        return HttpResponseRedirect('/login/')
    else:
        raise Exception("Not supported method to login!")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def profile(request):
    return render(request, 'profile.html', {})
