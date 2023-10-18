from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    class TitleChoose(models.TextChoices):
        programming = ('برنامه نویسی'),
        Artificial_Intelligence = ('هوش مصنوعی'),
        Electronics = ('لوازم الترونیکی'),
        internet = ('اینترنت'),
        security_and_network = ('امنیت و شبکه'),
        computer_and_hardware = ('کامپیوتر و سخت افزار'),
        software_and_application = ('نرم افزار و اپلیکیشن')
        
    title_choose = models.CharField(_('انتخاب عنوان دسته بندی'), max_length=24,
        choices=TitleChoose.choices,
        default=None
    )
    # parent_category = models.ForeignKey(
    #     'self',
    #     blank=True,
    #     null=True,
    #     on_delete=models.PROTECT,
    #     verbose_name=_('انتخاب زیر مجموعه دسته بندی'),
    #     related_name='children'
    # )
    category = models.CharField(_('انتخاب دسته بندی'),
        max_length=100,
        null=True,
        blank=True
    )
    create_category = jmodels.jDateTimeField(_('تاریخ ایجاد شده دسته بندی'),
                                             auto_now_add=True)
    
    class StatusSubCategory(models.TextChoices):
        published = 'pb', _('انتشار یافته')
        reject = 'rj', _('رد شده')
    status_category = models.CharField(_('وضعیت انشتار'),
        choices=StatusSubCategory.choices,
        max_length=2,
        null=True,
        blank=True
    )
    
    def __str__(self) -> str:
        return self.title_choose
    
    # def category_published(self):
    #     return self.title_choose.filter(status='published')
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        db_table = 'category'
        # ordering = ('title_choose',)