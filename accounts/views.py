from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.

@login_required
def index(request):
    # if request.user.is_authenticated:
    #     if_login = True
    #     user = request.user.username
    # else:
    #     if_login = False
    #     user = None
    #     return HttpResponseRedirect('/accounts/login')
    context = {
        # "if_login": if_login,
        # "user": user,
    }
    return render(request, 'accounts/index.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        # next_page = request.POST.get('post_id')
        if request.method == 'POST':
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
    # return HttpResponseRedirect('/')
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

@login_required
def logout_view(request):
    # return HttpResponse('<h1>This is Home<h1>')
    # if not request.user.is_authenticated:
    #     if_login = False
    #     user = None
    #     return HttpResponseRedirect('/accounts')
    # else:
    #     if_login = True
    #     logout(request)
    #     print("logout")
    #     user = request.user.username
    #     return HttpResponseRedirect('/')
    logout(request)
    context = {
        # "if_login": if_login,
        # "user": user,
    }
    # return render(request, 'accounts/logout.html', context)
    return HttpResponseRedirect('/')


def signup_view(request):
    if request.user.is_authenticated:
        if_login = True
        user = request.user.username
        return HttpResponseRedirect('/')
        # return index(request)
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                # username = form.cleaned_data.get("username")
                # password = form.cleaned_data.get("password")
                # user = authenticate(username=username, password=password)
                form.save()
                # if user is not None:
                #     login(request, user)
                print("Form is Valid")
                # return reverse("accounts:login_view")
                return HttpResponseRedirect(reverse("accounts:login_view"))
                # return HttpResponseRedirect('/accounts/login/')
            else:
                messages.error(
                    request, 'User Not Created!')
        if_login = False
        user = None
    form = form = UserCreationForm()
    context = {
        # "if_login": if_login,
        # "user": user,
        "form": form,
    }
    return render(request, 'accounts/signup.html', context)
