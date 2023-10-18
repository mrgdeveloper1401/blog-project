from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import PostModel, CategoryModel
from django.core.paginator import Paginator
# from django.views.generic import ListView


class HomeView(View):
    templated_name = 'posts/home.html'
    def get(self, request):
        all_post = PostModel.published.order_by('-created_at')[:10]
        category = CategoryModel.objects.all()
        
        paginator = Paginator(all_post, 1)
        page_number = request.GET.get('page')
        all_post = paginator.get_page(page_number)
        
        context = {
            'post': all_post,
            'category': category,
        }
        return render(request, self.templated_name, context)


class DetailsPostHomeView(View):
    template_name = 'posts/post_details.html'
    def get(self, request, *args, **kwargs):
        form = get_object_or_404(PostModel.published, pk=kwargs['post_id'], slug=kwargs['post_slug'])
        return render(request, self.template_name, {'form': form})
    

