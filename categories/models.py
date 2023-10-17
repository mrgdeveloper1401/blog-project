from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    title_choices = (
        ('programming', ('برنامه نویسی')),
        ('Artificial Intelligence', ('هوش مصنوعی')),
        ('Electronics', ('لوازم الترونیکی')),
        ('internet', ('اینترنت')),
        ('security nad network', ('امنیت و شبکه')),
        ('computer and hardware', ('کامپیوتر و سخت افزار')),
        ('software and application', ('نرم افزار و اپلیکیشن'))
    )
    title_choose = models.CharField(_('انتخاب نوع دسته بندی'), max_length=24,
                                    choices=title_choices,
                                    )
    create_category = jmodels.jDateTimeField(_('تاریخ ایجاد شده دسته بندی'),
                                             auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title_choose
    
    # def category_published(self):
    #     return self.title_choose.filter(status='published')
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        db_table = 'category'
        # ordering = ('title_choose',)