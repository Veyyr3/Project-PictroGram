from django.shortcuts import render, redirect
from django.urls import reverse # возвращает через name, spacename нужный url путь автоматически

# формочки
from image.forms import AddPublication

# сообщения
from django.contrib import messages

# модель
from image.models import Images

# главная страница
def index(request):
    return render(request, 'image/index.html')

# добавление публикации
def add_publication(request):
    if request.method == 'POST':
        form = AddPublication(data=request.POST, files=request.FILES) # то заполнить данными, которые написал пользователь в переменную request

        # если форма валидна
        if form.is_valid():
            publication = form.save(commit=False)
            publication.user = request.user
            publication.save()

            messages.success(request, 'Вы успешно добавили публикацию!')
            return redirect(reverse('image:add_publication'))
        else: # если нет
            messages.error(request, 'У вас есть ошибки!')
            return redirect(reverse('image:add_publication'))
    else: # если запрос гет
        form = AddPublication() # показать форму для добавлении публикации
    
    context = {
        'form': form,
    }

    return render(request, 'image/add_image.html', context)
