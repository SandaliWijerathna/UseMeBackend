# Generated by Django 3.0.5 on 2020-10-27 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='Password',
            new_name='password',
        ),
    ]
