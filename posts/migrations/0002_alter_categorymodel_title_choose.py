# Generated by Django 4.2.6 on 2023-10-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='title_choose',
            field=models.CharField(choices=[('تکنولوژی', 'تکنولوژی'), ('سبک زندگی', 'سبک زندگی')], max_length=10, verbose_name='انتخاب نوع دسته بندی'),
        ),
    ]
