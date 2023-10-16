from django.contrib import admin
from .models import Comment



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'post')
    list_display = ('id', 'user', 'updated_at', 'created_at', 'is_active',)
    list_editable = ('is_active',)
    list_filter = ('is_active','created_at', 'updated_at')
    list_display_links = ('id', 'user')
    search_fields = ('body', 'updated_at')
    prepopulated_fields = {'slug': ('body',)}