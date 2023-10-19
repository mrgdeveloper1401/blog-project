from django.contrib import admin
from .models import CategoryModel, SubCategoryModel



@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title_choose', 'category_str', 'status_category', 'create_category')
    list_editable = ('status_category', )

    def category_str(self, obj):
        return ','.join([i.category for i in obj.category.all()])



@admin.register(SubCategoryModel)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'created_sub_category', 'choose_sub_category')
    list_editable = ('choose_sub_category', )