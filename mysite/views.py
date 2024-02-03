
from django.http import HttpResponse, JsonResponse


def http_test(request):
    return HttpResponse('<h1>This is a test<h1>')

def json_test(request):
    return JsonResponse({
        'h1':'This is a h1',
        'h2':'This is a h2',
        })