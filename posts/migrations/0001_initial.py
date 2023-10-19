# Generated by Django 4.2.6 on 2023-10-18 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/post%Y/%M/%D', verbose_name='عکس')),
            ],
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=100, verbose_name='اختصار عنوان')),
                ('body', models.TextField(help_text='write any thing')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now, verbose_name='updated post')),
                ('status_choose', models.CharField(choices=[('pb', 'انتشار یافته'), ('rj', 'رد شده')], default='pb', max_length=2, verbose_name='انتخاب وضعیت')),
                ('category', models.ManyToManyField(related_name='categories', to='categories.categorymodel')),
                ('image', models.ManyToManyField(blank=True, related_name='images', to='posts.imagemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'مقاله و پست',
                'verbose_name_plural': 'مقالات و پست ها',
                'db_table': 'post',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='PostTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ManyToManyField(related_name='tags', to='posts.postmodel')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها',
            },
        ),
        migrations.AddIndex(
            model_name='postmodel',
            index=models.Index(fields=['-created_at'], name='post_created_f85ddb_idx'),
        ),
    ]
