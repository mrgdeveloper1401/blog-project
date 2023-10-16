from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from accounts.models import Users
from posts.models import Post


class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField(max_length=300)
    slug = models.SlugField(unique=True)
    image = models.ImageField(_("عکس"), upload_to='comments/%Y/%M/%D')
    video = models.FileField(_("فیلم"), upload_to='comments/%Y/%M/%D')
    is_active = models.BooleanField(default=True)
    created_at = jmodels.jDateTimeField(_('تاریخ ایجاد کامنت'), auto_now_add=True)
    updated_at = jmodels.jDateTimeField(_('تاریخ بروزرسانی کامنت'),auto_now=True)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply_to_comments')
    
    
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
        db_table = 'comment'
        

        
        
