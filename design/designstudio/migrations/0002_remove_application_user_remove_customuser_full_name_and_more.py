# Generated by Django 4.2.7 on 2023-11-05 17:02

import designstudio.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designstudio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='full_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default=2, max_length=254, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.TextField(default='something', max_length=1000),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='photo_file',
            field=models.ImageField(max_length=254, upload_to='images', validators=[designstudio.models.Application.validate_image, django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])]),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=254, verbose_name='Выбор категории'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=254, unique=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=254, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=254, unique=True, verbose_name='Логин'),
        ),
    ]
