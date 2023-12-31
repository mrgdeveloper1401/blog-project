# Generated by Django 4.2.6 on 2023-10-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_remove_categorymodel_category_categorymodel_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='دسته بندی')),
            ],
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category',
            field=models.ManyToManyField(related_name='sub_categorys', to='categories.subcategorymodel'),
        ),
    ]
