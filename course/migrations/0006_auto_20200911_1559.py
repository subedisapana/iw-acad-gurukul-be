# Generated by Django 3.1 on 2020-09-11 15:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0005_auto_20200828_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
