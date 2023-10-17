from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Users
from django_jalali.db import models as jmodels
from categories.models import CategoryModel


# post managers
class PostManagers(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status_choose=PostModel.StatusPost.published)
    

class ImageModel(models.Model):
    image = models.ImageField(_('عکس'),
                              upload_to='images/post%Y/%M/%D')

class PostModel(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='posts')
    category = models.ManyToManyField(CategoryModel, 
                                 related_name='categories')
    image = models.ManyToManyField(ImageModel, related_name='images',
                                   blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField(help_text='write any thing')
    slug = models.SlugField(null=True, unique=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(_('updated post'), default=timezone.now)
    
    
    class StatusPost(models.TextChoices):
        published = 'pb', _('انتشار یافته')
        reject ='rj', _('رد شده')
        
        
    status_choose = models.CharField(_('انتخاب وضعیت'), max_length=2,
                                    choices=StatusPost.choices,
                                    default=StatusPost.published)
    objects = models.Manager()
    published = PostManagers()
    
    
    def __str__(self) -> any:
        return self.title
    
    
    def get_absolute_url(self):
        return reverse_lazy("posts:details_post", args=(self.pk, self.slug))


    
    class Meta:
        verbose_name = 'مقاله و پست'
        verbose_name_plural = 'مقالات و پست ها'
        db_table = 'post'
        ordering = ('-created_at', )
        indexes = (
            models.Index(fields=['-created_at',]),
        )
    
    
# class PostImageModel(models.Model):
#     user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='posts')
#     image = models.ManyToManyField(PostModel, related_name='post_images')
    
class PostTagModel(models.Model):
    title = models.ManyToManyField(PostModel, related_name='tags')


    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'