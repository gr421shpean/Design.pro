from django import forms
from django.core.exceptions import ValidationError
import re


from .models import CustomUser





class Registration(forms.Form):
    username = forms.CharField(label='Логин (латиница и дефис)', max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    full_name = forms.CharField(label='ФИО', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ваше ФИО'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'placeholder': 'example@example.com'}))
    password = forms.CharField(label='Пароль', max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password_confirm = forms.CharField(label='Повторите пароль', max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
    agree_to_processing = forms.BooleanField(label='Согласие на обработку персональных данных', required=True)
    error_css_class = "error"
    required_css_class = "field"

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if not re.match(r'^[а-яёА-ЯЁ\s-]+$', full_name):
            raise ValidationError("ФИО может содержать только кириллические буквы, дефис и пробелы.")
        return full_name

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[a-zA-Z-]+$', username):
            raise ValidationError("Логин может содержать только латиницу и дефис.")
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Пользователь с таким логином уже существует.")
        return username

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            self.add_error('', "Пароли не совпадают.")
        return password_confirm

    class Meta:
        model = CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин (латиница и дефис)', max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))




