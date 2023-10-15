from django.contrib import admin
from .models import Post



@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('user', 'is_active', 'created_at', 'updated_at')
    list_editable = ('is_active', )
    