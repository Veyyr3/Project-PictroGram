# image/forms.py

# для красивых формочек (инструменты для frontend)
from django import forms

# импортировать модель
from image.models import Images

# форма для создания публикации
class AddPublication(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'button-green-confirm to-left',
    }))

    image_name = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength': 30,
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'style': 'resize: none;',
        'rows': 10,
    }))

    class Meta:
        model = Images
        fields = ['image', 'image_name', 'description']
