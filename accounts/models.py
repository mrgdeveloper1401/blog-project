from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels
from django.utils import timezone


class Users(AbstractUser):
    email = models.EmailField(_("ایمیل"), max_length=254, unique=True)
    mobile_phone = models.CharField(_('شماره همراه'), max_length=11, unique=True, blank=True,
                                    null=True)
    gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    date_joined = jmodels.jDateTimeField(_("date joined"), default=timezone.now)
    last_login = jmodels.jDateTimeField(_("last login"), blank=True, null=True)
    gender = models.CharField(_('Gender'), max_length=6, choices=gender, default='Male')
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        db_table = 'user'
        

class Notification(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='notifications')
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body
    
    
    class Meta:
        verbose_name = 'اعلان'
        verbose_name_plural = 'اعلانات'
        db_table = 'notifications'