from django.contrib import admin
from .models import CategoryModel



@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title_choose', 'category', 'status_category', 'create_category')
    list_display_links = ('category',)
    list_editable = ('title_choose', 'status_category')