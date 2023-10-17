from django.contrib import admin
from .models import Users, Notification
from django.contrib.auth.admin import UserAdmin
from django_jalali.admin.filters import JDateFieldListFilter
from django.utils.translation import gettext_lazy as _


@admin.register(Users)
class UserAdmin(UserAdmin):
    ordering = ('date_joined',)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "username", "mobile_phone")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display_links = ('username', 'email')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created_at', 'is_active')
    search_fields = ('body', 'user')
    list_filter = ('is_active',('created_at', JDateFieldListFilter))
    list_editable = ('is_active',)