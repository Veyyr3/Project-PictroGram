# users/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages # messages - флешка
from django.urls import reverse # возвращает через name, spacename нужный url путь автоматически
from django.http import HttpResponseForbidden
from django.db.models import Count, Exists, OuterRef

# декоратор доступа
from django.contrib.auth.decorators import login_required

# импорт формы
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

# импорт модели
from image.models import Images, Likes
from users.models import User, Subscriptions

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
                print(f"Пользователь найден: {user.username}") # Отладка
                auth.login(request, user) # авторизуем пользователя
                print("Пользователь авторизован.") # Отладка
                return redirect(reverse('users:profile')) # перенаправляем пользователя
            else:
                print("form.get_user() вернул None (пользователь не найден).")
        else:
            print("Форма авторизации НЕ валидна. Ошибки:", form.errors) # Отладка
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
            messages.success(request, 'Поздравляем! Вы успешно зарегистрировались! Теперь войдите в систему.') # сказать пользователю об успехе изменения данных
            return redirect(reverse('users:login'))
    else: # если гет запрос
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/registration.html', context) # перенаправление на авторизацию

# посмотреть профиль другого пользователя
@login_required
def profile_other(request, user_id):
    # данный пользователь
    this_user = get_object_or_404(User, id=user_id)

    # список его публикации
    publications_queryset = Images.objects.filter(user=user_id).order_by('-created_at')

    # добавить к публикациям доп поля
    publications = publications_queryset.annotate(
        # Подсчет лайков для каждой публикации
        like_count=Count('image_likes'), # 'image_likes' - это related_name или дефолтное имя для ForeignKey

        # Проверка, лайкнул ли ТЕКУЩИЙ пользователь эту публикацию
        # OuterRef позволяет ссылаться на поле из внешнего запроса
        # Exists проверяет наличие связанного объекта без полной его загрузки
        is_liked_by_user=Exists(
            Likes.objects.filter(
                image=OuterRef('pk'), # 'pk' относится к текущей публикации во внешнем запросе
                user=request.user      # Проверяем на текущего пользователя
            )
        )
    )

    # кол-во подписчиков
    subscribers_count = this_user.subscribers.count()

    # Сделал ли ТЕКУЩИЙ АВТОРИЗОВАННЫЙ пользователь подписку на ЭТОГО пользователя
    is_subscribed = False # По умолчанию считаем, что подписки нет

    # если пользователь авторизован
    if request.user.is_authenticated:
        # проверяем существует ли запись
        is_subscribed = Subscriptions.objects.filter(
            subscriber=request.user,
            subscribed_to=this_user
        ).exists()

    context = {
        'this_user': this_user,
        'publications': publications,
        'is_subscribed': is_subscribed,
        'subscribers_count': subscribers_count,
    }
    return render(request, 'users/profile_other.html', context)

# показать профиль пользователя
@login_required
def profile (request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES) # заполнить форму данными, которые пользователь запросил, а после заполнить новую форму данными, которые ввел пользователь.
        # files=request.FILES для работы с файлами, изображениями и т.д.
        
        # если форма валидна
        if form.is_valid():
            form.save() # сохранить данные
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect(reverse('users:profile')) # перенаправляем на ту же страницу, но с обновленными данными
        # если нет
        else:
            messages.error(request, 'Ошибка при обновлении профиля. Проверьте введенные данные.')
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user) # показать пользователю форму и заполнить её данными о пользователе

    # взять те фото, которые добавил пользователь
    images_queryset = Images.objects.filter(user=request.user).order_by('-created_at')

    # добавляем доп. поле для подсчета лайков
    images = images_queryset.annotate(
        like_count=Count('image_likes'),
    )

    # посчитать кол-во подписчиков для пользователя
    subscriber_count = request.user.subscribers.count()

    context = {
        'form': form, 
        'images': images,
        'subscriber_count': subscriber_count,
    }
    return render(request, 'users/profile.html', context)

# выйти
def logout (request):
    auth.logout(request)
    return redirect(reverse('image:index'))

# удалить публикацию
def delete_publication (request, image_id):
    if request.method == 'POST':
        image = get_object_or_404(Images, id=image_id)

        # если этот бро не этот бро
        if image.user != request.user:
            messages.error(request, 'У вас нет прав для удаления этой публикации.')
            return HttpResponseForbidden("У вас нет прав для удаления этой публикации.")
        
        image.delete()
        messages.success(request, 'Публикация успешно удалена.')

    return redirect(reverse('users:profile'))

# посмотреть свои подписки
def subscriptions(request):
    # все подписки пользователя
    all_subscriptions = Subscriptions.objects.filter(subscriber=request.user)

    # число подписок
    count_subscriptions = request.user.subscriptions_made.count()

    context = {
        'all_subscriptions': all_subscriptions,
        'count_subscriptions': count_subscriptions,
    }

    return render(request, 'users/subscriptions.html', context)

# подписаться на кого-нибудь
def subscribe(request, user_id):
    # пользователь на которого подписываются
    user_subscribed_to = User.objects.get(id=user_id)

    # создать подписку
    subscribe, subscribe_created = Subscriptions.objects.get_or_create(subscriber=request.user, subscribed_to=user_subscribed_to)

    # проверка подписки
    if subscribe_created:
        messages.success(request,'Вы успешно подписались на пользователя!')
    else:
        messages.error(request,'Возникли ошибки, когда вы попытались подписаться.')
        
    return redirect(reverse('users:profile_other', kwargs={'user_id': user_subscribed_to.id}))

# отписаться
def unsubscribe(request, user_id):
    # пользователь на которого отписываются
    user_subscribed_to = User.objects.get(id=user_id)

    # подписка
    subscription = Subscriptions.objects.get(subscriber=request.user, subscribed_to=user_subscribed_to)

    subscription.delete()

    messages.success(request,'Вы успешно отписались от пользователя!')

    next_url = request.META.get('HTTP_REFERER')
    if not next_url:
        return redirect(reverse('users:profile_other', kwargs={'user_id': user_subscribed_to.id}))

    return redirect(next_url)
