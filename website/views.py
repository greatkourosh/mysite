
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from website.forms import NameForm, ContactForm, NewsletterForm


def index(request):
    # return HttpResponse('<h1>This is Home<h1>')
    return render(request, 'website/index.html')


def home(request):
    return index()


def about(request):
    # return HttpResponse('<h1>This is about<h1>')
    return render(request, 'website/about.html')


def contact(request):
    # return HttpResponse('<h1>This is contact<h1>')
    if request.method == 'POST':
        # print('Post request')
        # name = request.POST.get('name')
        # subject = request.POST.get('subject')
        # email = request.POST.get('email')
        # message = request.POST.get('message')
        # print(f'name: {name}, subject: {subject}, email: {email}, message: {message}')
        # c = Contact()
        # c.name = name
        # c.subject = subject
        # c.email = email
        # c.message = message
        # c.save()
        # print(name)
        # form = NameForm(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
            # messages.add_message(request, messages.SUCCESS, 'Your Message has been sent successfully!')
            messages.success(
                request, 'Your Message has been sent successfully!')
            # return HttpResponse(f"Thanks for {name}, {subject}, {email} and {message}")
        else:
            # messages.add_message(request, messages.ERROR, 'Your Message has not been sent successfully!')
            messages.warning(
                request, 'Your Message has not been sent successfully!')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'website/contact.html', context)


def newsletter(request):
    # return HttpResponse('<h1>This is contact<h1>')
    if request.method == 'POST':
        # print('Post request')
        # name = request.POST.get('name')
        # subject = request.POST.get('subject')
        # email = request.POST.get('email')
        # message = request.POST.get('message')
        # print(f'name: {name}, subject: {subject}, email: {email}, message: {message}')
        # c = Contact()
        # c.name = name
        # c.subject = subject
        # c.email = email
        # c.message = message
        # c.save()
        # print(name)
        # form = NameForm(request.POST)
        form = NewsletterForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # subject = form.cleaned_data['subject']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            form.save()
            # return HttpResponse(f"Thanks for {name}, {subject}, {email} and {message}")
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    # return render(request, 'website/contact.html', context)


def test_view(request):
    context = {'name': 'Gamba Ozaka'}
    return render(request, 'website/test_view.html', context)


def test(request):
    if request.method == 'POST':
        # print('Post request')
        # name = request.POST.get('name')
        # subject = request.POST.get('subject')
        # email = request.POST.get('email')
        # message = request.POST.get('message')
        # print(f'name: {name}, subject: {subject}, email: {email}, message: {message}')
        # c = Contact()
        # c.name = name
        # c.subject = subject
        # c.email = email
        # c.message = message
        # c.save()
        # print(name)
        # form = NameForm(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
            return HttpResponse(f"Thanks for {name}, {subject}, {email} and {message}")
    else:
        form = ContactForm()
    context = {
        'name': 'Gamba Ozaka',
        'form': form
    }
    return render(request, 'website/test.html', context)
