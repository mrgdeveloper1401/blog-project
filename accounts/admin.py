from django.contrib import admin
from .models import Users, Notification
from django.contrib.auth.admin import UserAdmin
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(Users)
class UserAdmin(UserAdmin):
    ordering = ('date_joined',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created_at', 'is_active')
    search_fields = ('body', 'user')
    list_filter = ('is_active',('created_at', JDateFieldListFilter))
    list_editable = ('is_active',)