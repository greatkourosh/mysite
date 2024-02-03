
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


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

def http_test(request):
    return HttpResponse('<h1>This is a test<h1>')

def json_test(request):
    return JsonResponse({
        'h1':'This is a h1',
        'h2':'This is a h2',
        })