from django.contrib import admin
from .models import Post



@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('user', 'body'[:30], 'updated_at', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('body', )
    list_editable = ('is_active', )
    raw_id_fields = ('user', )
    prepopulated_fields = {'slug': ('body',)}
    ordering = ('-created_at', )