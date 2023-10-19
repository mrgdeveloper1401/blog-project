from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _


class TicketMoel(models.Model):
    first_name = models.CharField(_('نام'), max_length=100)
    last_name = models.CharField(_('خانوادگی'), max_length=100)
    email = models.EmailField(_("ایمیل"), unique=True)
    created_at_ticket = jmodels.jDateTimeField(_('تاریخ ایجاد تیکت'), auto_now_add=True)
    body = models.TextField(_('متن تیکت'))
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = _("تیکت")
        verbose_name_plural = _("تیکت ها")
        db_table = 'ticket'
        
