from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        # -27- Указываем email и остальные три поля из ТЗ
        fields = ('email', 'phone', 'country', 'avatar')

        # -27- Стилизуем дополнительные поля формы крупными классами Bootstrap
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'example@mail.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '+7...'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Страна'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # -27- Стилизуем поля паролей крупными классами Bootstrap и добавляем подсказку про 8 символов
        if 'password1' in self.fields:
            self.fields['password1'].widget.attrs.update({
                'class': 'form-control form-control-lg',
                'placeholder': 'Введите пароль не менее 8 символов'
            })
            self.fields['password1'].label = 'Пароль'

        if 'password2' in self.fields:
            self.fields['password2'].widget.attrs.update({
                'class': 'form-control form-control-lg',
                'placeholder': 'Повторите пароль'
            })
            self.fields['password2'].label = 'Подтверждение пароля'


# -27- Форма для редактирования профиля пользователя (также увеличиваем поля)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'country', 'avatar')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }
