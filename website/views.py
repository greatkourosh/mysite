
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse('<h1>Homepage<h1>')

def home(request):
    return index()

def about(request):
    return HttpResponse('<h1>This is about<h1>')

def contact(request):
    return HttpResponse('<h1>This is contact<h1>')

def http_test(request):
    return HttpResponse('<h1>This is a test<h1>')

def json_test(request):
    return JsonResponse({
        'h1':'This is a h1',
        'h2':'This is a h2',
        })