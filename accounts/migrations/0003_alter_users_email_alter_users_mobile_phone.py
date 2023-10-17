# Generated by Django 4.2.6 on 2023-10-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_users_mobile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='users',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='شماره همراه'),
        ),
    ]