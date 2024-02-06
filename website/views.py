
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from mysite.settings import BASE_DIR, STATIC_ROOT, STATIC_URL
from website.models import Contact
from website.forms import NameForm

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
    return render(request, 'website/contact.html')

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
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return HttpResponse(f"Thanks for {name}, {subject}, {email} and {message}")
    else:
        form = NameForm()
    context = {
        'name': 'Gamba Ozaka',
        'form': form
        }
    return render(request, 'website/test.html', context)