# Generated by Django 4.2.7 on 2023-11-09 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designstudio', '0005_application_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]
