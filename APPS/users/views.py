# users/views.py
from django.shortcuts import render, redirect
from django.contrib import auth, messages # messages - флешка
from django.urls import reverse # возвращает через name, spacename нужный url путь автоматически

# импорт формы
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

# авторизация пользователя
def login (request):
    # если запрос пост
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST) # то заполнить данными, которые написал пользователь в переменную request

        # если форма валидна
        if form.is_valid():
            # AuthenticationForm имеет метод get_user(), который возвращает аутентифицированного пользователя
            user = form.get_user()

            # если пользователь есть в системе по аутетифицированным полям
            if user:
                auth.login(request, user) # авторизуем пользователя
                return redirect(reverse('users:profile')) # перенаправляем пользователя
    else: # если запрос гет
        form = UserLoginForm() # показать форму для регистрации

    # вывод словаря
    context = {'form': form}
    return render(request, 'users/login.html', context)

# регистрация пользователя
def registration (request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST) # то заполнить данными, которые написал пользователь в переменную request

        # если форма валидна
        if form.is_valid():
            form.save() # сохранить данные
            messages.success(request, 'Поздравляем! Вы успешно зарегистрировались! Теперь войдите в систему') # сказать пользователю об успехе изменения данных
            return redirect(reverse('users:login'))
    else: # если гет запрос
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/registration.html', context) # перенаправление на авторизацию

# показать профиль пользователя
def profile (request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES) # заполнить форму данными, которые пользователь запросил, а после заполнить новую форму данными, которые ввел пользователь.
        # files=request.FILES для работы с файлами, изображениями и т.д.
        
        # если форма валидна
        if form.is_valid():
            form.save() # сохранить данные
            return redirect(reverse('users:profile')) # перенаправляем на ту же страницу, но с обновленными данными
        # если нет
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user) # показать пользователю форму и заполнить её данными о пользователе
    
    context = {'form': form}
    return render(request, 'users/profile.html', context)

# выйти
def logout (request):
    auth.logout(request)
    return redirect(reverse('image:index'))

# профиль других
def profile_other(request):
    return render(request, 'users/profile_other.html')

# подписки
def subscriptions(request):
    return render(request, 'users/subscriptions.html')