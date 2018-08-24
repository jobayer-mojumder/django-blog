from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'cadmin/login.html', {'message': None})
    else:
        return render(request, 'cadmin/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('cadmin_index'))
        else:
            return render(request, 'cadmin/login.html', {'message': 'User not found!'})
    else:
        return render(request, 'cadmin/login.html', {'message': "Please Login!"})


def logout_view(request):
    logout(request)
    return render(request, 'cadmin/login.html', {'message': "Successfully Logout!"})
