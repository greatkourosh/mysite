
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from mysite.settings import BASE_DIR, STATIC_ROOT, STATIC_URL


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