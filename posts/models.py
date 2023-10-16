from django.urls import reverse_lazy
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Users
from django_jalali.db import models as jmodels


class Post(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='post/image', null=True, blank=True)
    video = models.FileField(upload_to='post/video', null=True, blank=True)
    body = models.TextField(help_text='write any thing', max_length=300)
    slug = models.SlugField(null=True, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(_('updated post'), default=timezone.now)
    
    # def __str__(self) -> any:
    #     return self.user
    
    def get_absolute_url(self):
        return reverse_lazy("posts:details_post", args=(self.pk, self.slug))
    
    
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        db_table = 'post'
        ordering = ('created_at',)
    
