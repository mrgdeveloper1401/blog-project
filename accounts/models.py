from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    mobile_phone = models.CharField(_('mobile'), max_length=11, unique=True)
    gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(_('Gender'), max_length=6, choices=gender, default='Male')
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'
        

class Notification(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='notifications')
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body
    
    
    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'
        db_table = 'notifications'