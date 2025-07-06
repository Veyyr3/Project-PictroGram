# users/forms.py

# для красивых формочек (инструменты для frontend)
from django import forms
# импортировать для наследования для формы авторизации/регистрации пользователей
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

# импортировать модель пользователя
from users.models import User

# форма для авторизации пользователей
class UserLoginForm (AuthenticationForm):
    # инпут для имя пользователя
    username = forms.CharField(widget=forms.TextInput(attrs= {
        # здесь атрибуты для тега TextInput
        'placeholder': 'Введите имя пользователя'
    })) # используя django forms задать атрибуты для frontend

    # инпут для пароля
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))

# форма регитсрации пользователей
class UserRegistrationForm(UserCreationForm):
    # инпут для имя
    first_name = forms.CharField(widget=forms.TextInput(attrs= {
        'placeholder': 'Введите имя'
    }))

    # инпут для фамилии
    last_name = forms.CharField(widget=forms.TextInput(attrs= {
        'placeholder': 'Введите фамилию'
    }))

    # логин/имя пользователя
    username = forms.CharField(widget=forms.TextInput(attrs= {
        'placeholder': 'Введите имя пользователя'
    }))

    # почта
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите адрес электронной почты'
    }))

    # введите пароль
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))

    # подтвердите пароль
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        # password1 -- введите пароль
        # password2 -- подтвердите пароль

# форма изменения формы 
class UserProfileForm(UserChangeForm):
    # логин/имя пользователя
    username = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength': 30,
    }))

    # расскажите о себе
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 10,
        'style': 'resize: none;'
    }), required=False)

    # изображение
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'bio', 'avatar']
