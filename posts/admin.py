from django.contrib import admin
from .models import PostModel, PostTagModel, CategoryModel
from django_jalali.admin.filters import JDateFieldListFilter



@admin.register(PostModel)
class Post(admin.ModelAdmin):
    list_display = ('user', 'updated_at', 'created_at', 'is_active')
    list_filter = ('is_active', ('created_at', JDateFieldListFilter),
                   ('updated_at', JDateFieldListFilter))
    search_fields = ('body', )
    list_editable = ('is_active', )
    raw_id_fields = ('user', )
    prepopulated_fields = {'slug': ('body',)}
    ordering = ('-created_at', )
    
    

@admin.register(PostTagModel)
class PostTagAdmin(admin.ModelAdmin):
    # list_display = ('title',)
    pass


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    pass