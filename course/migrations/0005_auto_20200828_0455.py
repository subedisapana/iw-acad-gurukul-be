# Generated by Django 3.1 on 2020-08-28 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20200827_0546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='user',
            new_name='users',
        ),
    ]
