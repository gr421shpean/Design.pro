from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


class CustomUser(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='ФИО', blank=False)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)


    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=254, verbose_name='Выбор категории', blank=False)

    def __str__(self):
        return self.category


class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default='something')
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name='Время создания заявки', auto_now_add=True)
    status = models.CharField(max_length=254, default='Новая')

    REQUEST_STATUS = (
        ('Новая', 'Новая'),
        ('Принята в работу', 'Принято в работу'),
        ('Выплнено', 'Выполнено'),
    )
    status = models.CharField(
        max_length=16,
        choices=REQUEST_STATUS,
        default='Новая',
        blank=True,
        verbose_name="Статус")


    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    photo_file = models.ImageField(max_length=254, upload_to='images', blank=False, validators=[validate_image, FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])])

    def get_absolute_url(self):
        return reverse('application_list', args=[str(self.id)])

    def __str__(self):
        return f'{self.name} ({self.date})'





