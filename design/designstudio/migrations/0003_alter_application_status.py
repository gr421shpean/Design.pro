# Generated by Django 4.2.7 on 2023-11-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designstudio', '0002_remove_application_user_remove_customuser_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(blank=True, choices=[('N', 'Новая'), ('P', 'Принято в работу'), ('C', 'Выполнено')], default='Новая', max_length=16, verbose_name='Статус'),
        ),
    ]