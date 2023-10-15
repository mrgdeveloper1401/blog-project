from django.contrib import admin
from .models import Users, Notification
from django.contrib.auth.admin import UserAdmin


@admin.register(Users)
class UserAdmin(UserAdmin):
    ...


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created_at', 'is_active')
    list_filter = ('is_active','created_at')
    list_editable = ('is_active',)