from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'users/profile.html')

def profile_other(request):
    return render(request, 'users/profile_other.html')