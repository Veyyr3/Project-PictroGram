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
    # инпут для имя
    first_name = forms.CharField(widget=forms.TextInput(attrs= {
        'class': 'form-control py-4',
    }))

    # инпут для фамилии
    last_name = forms.CharField(widget=forms.TextInput(attrs= {
        'class': 'form-control py-4',
    }))

    # логин/имя пользователя
    username = forms.CharField(widget=forms.TextInput(attrs= {
        'class': 'form-control py-4',
        'readonly': True
    }))

    # почта
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'readonly': True
    }))

    # изображение
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'image']