from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    title_choices = (
        ('texhnology', ('تکنولوژی')),
        ('lifestyle', ('سبک زندگی')),
    )
    title_choose = models.CharField(_('انتخاب نوع دسته بندی'), max_length=10,
                                    choices=title_choices,
                                    null=True, blank=True,
                                    default='----')
    create_category = jmodels.jDateTimeField(_('تاریخ ایجاد شده دسته بندی'),
                                             auto_now_add=True)
    category = models.CharField(_("انتخاب دسته بندی"), max_length=100, null=True,
                                blank=True)
    
    def __str__(self) -> str:
        return self.title_choose
    
    def category_published(self):
        return self.title_choose.filter(status='published')
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        db_table = 'category'
        # ordering = ('title_choose',)