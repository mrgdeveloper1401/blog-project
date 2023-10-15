from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Users


class Post(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='post/image',)
    video = models.FileField(upload_to='post/video')
    body = models.TextField(help_text='write any thing')
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(_('updated post'), default=timezone.now)
    
    def __str__(self) -> str:
        return self.user
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'post'
    
