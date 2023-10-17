from django.contrib import admin
from .models import PostModel, PostTagModel, CategoryModel
from django_jalali.admin.filters import JDateFieldListFilter



@admin.register(PostModel)
class Post(admin.ModelAdmin):
    list_display = ('user', 'category_to_str','updated_at', 'created_at', 'is_active',
                    'status_choose', 'category')
    list_filter = ('is_active', ('created_at', JDateFieldListFilter),
                   ('updated_at', JDateFieldListFilter))
    search_fields = ('body', )
    list_editable = ('is_active', 'status_choose')
    raw_id_fields = ('user', )
    prepopulated_fields = {'slug': ('body',)}
    ordering = ('-created_at', )
    filter_horizontal = ('category', 'image',)
    
    def category_to_str(self, obj):
        return [categories.title_choose for categories in obj.category.all() ]
    
    

@admin.register(PostTagModel)
class PostTagAdmin(admin.ModelAdmin):
    # list_display = ('title',)
    pass


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title_choose','create_category')
    list_display = ('title_choose', 'create_category')