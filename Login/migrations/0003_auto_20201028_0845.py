# Generated by Django 3.0.5 on 2020-10-28 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20201027_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]