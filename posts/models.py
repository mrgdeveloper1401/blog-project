from django.urls import reverse_lazy
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Users
from django_jalali.db import models as jmodels



class CategoryModel(models.Model):
    title_choices = (
        ('تکنولوژی', _('تکنولوژی')),
        ('سبک زندگی', _('سبک زندگی')),
    )
    title_choose = models.CharField(_('انتخاب نوع دسته بندی'), max_length=10,
                                    choices=title_choices)
    
    def __str__(self) -> str:
        return self.title_choose
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        db_table = 'category'
        # ordering = ('title_choose',)

class PostModel(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, 
                                 related_name='categories')
    title = models.CharField(max_length=255)
    body = models.TextField(help_text='write any thing')
    image = models.ImageField(_("عکس"), upload_to='posts/%Y/%M/%D', blank=True, null=True)
    slug = models.SlugField(null=True, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(_('updated post'), default=timezone.now)
    
    def __str__(self) -> any:
        return self.body
    
    def get_absolute_url(self):
        return reverse_lazy("posts:details_post", args=(self.pk, self.slug))
    
    
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        db_table = 'post'
        ordering = ('created_at',)
    
    
# class PostImageModel(models.Model):
#     user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='posts')
#     image = models.ManyToManyField(PostModel, related_name='post_images')
    
class PostTagModel(models.Model):
    title = models.ManyToManyField(PostModel, related_name='tags')


    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'