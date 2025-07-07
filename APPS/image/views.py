from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse # возвращает через name, spacename нужный url путь автоматически
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# формочки
from image.forms import AddPublication

# сообщения
from django.contrib import messages

# модель
from image.models import Images, Likes

# главная страница
def index(request):
    # публикации
    publications = Images.objects.all().order_by('-created_at')

    context = {
        'publications': publications,
    }

    return render(request, 'image/index.html', context)

# добавление публикации
@login_required
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

# поставить лайк
@login_required
def like(request, image_id):
    # фото на которое надо поставить лайк
    image = get_object_or_404(Images, id=image_id)

    like, is_liked = Likes.objects.get_or_create(user=request.user, image=image)

    # если поставили лайк
    if is_liked:
        messages.success(request, 'Вы поставили лайк!')
    else: # если лайк был
        like.delete()
        messages.success(request, 'Вы удалили лайк!')

    return redirect(reverse('image:index'))