# Generated by Django 4.2.6 on 2023-10-18 08:24

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_choose', models.CharField(choices=[('برنامه نویسی', 'Programming'), ('هوش مصنوعی', 'Artificial Intelligence'), ('لوازم الترونیکی', 'Electronics'), ('اینترنت', 'Internet'), ('امنیت و شبکه', 'Security And Network'), ('کامپیوتر و سخت افزار', 'Computer And Hardware'), ('نرم افزار و اپلیکیشن', 'Software And Application')], default=None, max_length=24, verbose_name='انتخاب عنوان دسته بندی')),
                ('category', models.CharField(max_length=100, verbose_name='انتخاب دسته بندی')),
                ('create_category', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده دسته بندی')),
                ('status_category', models.CharField(choices=[('pb', 'انتشار یافته'), ('rj', 'رد شده')], max_length=2, verbose_name='وضعیت انشتار')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'db_table': 'category',
            },
        ),
    ]
