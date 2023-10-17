from django.contrib import admin
from .models import PostModel, PostTagModel
from django_jalali.admin.filters import JDateFieldListFilter



@admin.register(PostModel)
class Post(admin.ModelAdmin):
    list_display = ('user', 'category_to_str','updated_at', 'created_at', 'status_choose')
    list_filter = ('status_choose', ('created_at', JDateFieldListFilter),
                   ('updated_at', JDateFieldListFilter))
    search_fields = ('body', )
    list_editable = ('status_choose', 'status_choose')
    raw_id_fields = ('user', )
    prepopulated_fields = {'slug': ('body',)}
    ordering = ('-created_at', )
    filter_horizontal = ('category', )
    date_hierarchy = 'created_at'
    
    def category_to_str(self, obj):
        return [categories.title_choose for categories in obj.category.all() ]
    
    

@admin.register(PostTagModel)
class PostTagAdmin(admin.ModelAdmin):
    # list_display = ('title',)
    pass
