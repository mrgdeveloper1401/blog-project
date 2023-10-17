from django.contrib import admin
from .models import CategoryModel



@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title_choose','create_category')
    list_display = ('title_choose', 'create_category')
    # ordering = ('', )