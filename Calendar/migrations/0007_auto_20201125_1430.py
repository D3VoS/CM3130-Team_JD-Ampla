# Generated by Django 3.1.3 on 2020-11-25 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Calendar', '0006_auto_20201125_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventCreator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Accounts.user'),
            preserve_default=False,
        ),
    ]
