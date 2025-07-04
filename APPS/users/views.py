from django.shortcuts import render

# главный профиль
def profile(request):
    return render(request, 'users/profile.html')

# профиль других
def profile_other(request):
    return render(request, 'users/profile_other.html')

# подписки
def subscriptions(request):
    return render(request, 'users/subscriptions.html')
