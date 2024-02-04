from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    context = {'title': 'Gamba', 'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor', 'author': 'ASghar Farhadi'}
    return render(request, 'blog/blog-single.html', context)