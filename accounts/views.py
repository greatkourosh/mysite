from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        if_login = True
        user = request.user.username
    else:
        if_login = False
        user = None
        return HttpResponseRedirect('/accounts/login')
    context = {
        # "if_login": if_login,
        # "user": user,
    }
    return render(request, 'accounts/index.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # user = authenticate(request, username=username, password=password)
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/accounts')
                else:
                    messages.error(
                        request, 'User Not Found!')
    # if request.user.is_authenticated:
    #     if_login = True
    #     user = request.user.username
    #     return HttpResponseRedirect('/accounts')
    #     # return index(request)
    # else:
    #     if_login = False
    #     user = None
    form = AuthenticationForm()
    context = {
        'form': form,
        # "if_login": if_login,
        # "user": user,
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    # return HttpResponse('<h1>This is Home<h1>')
    if not request.user.is_authenticated:
        if_login = False
        user = None
        return HttpResponseRedirect('/accounts')
    else:
        if_login = True
        logout(request)
        print("logout")
        user = request.user.username
        return HttpResponseRedirect('/')
    context = {
        # "if_login": if_login,
        # "user": user,
    }
    return render(request, 'accounts/logout.html', context)


def signup_view(request):
    if request.user.is_authenticated:
        if_login = True
        user = request.user.username
        return HttpResponseRedirect('/accounts')
        # return index(request)
    else:
        if_login = False
        user = None
    context = {
        # "if_login": if_login,
        # "user": user,
    }
    return render(request, 'accounts/signup.html', context)
