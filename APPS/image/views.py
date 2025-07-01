from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'image/index.html')

def add_publication(request):
    return render(request, 'image/add_image.html')
