# Generated by Django 3.1.3 on 2020-11-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='email address'),
        ),
    ]
