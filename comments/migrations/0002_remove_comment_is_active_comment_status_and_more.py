# Generated by Django 4.2.6 on 2023-10-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_active',
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('pb', 'انشار یافته'), ('rj', 'رد شده')], default='pb', max_length=2),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=300, verbose_name='متن کامنت'),
        ),
    ]
