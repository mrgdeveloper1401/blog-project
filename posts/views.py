from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import PostModel, CategoryModel


class HomeView(View):
    templated_name = 'posts/home.html'
    def get(self, request):
        all_post = PostModel.objects.published().order_by('-created_at')[:10]
        category = CategoryModel.objects.all()
        context = {
            'home': all_post,
            'category': category,
        }
        return render(request, self.templated_name, context)


class DetailsPostHomeView(View):
    template_name = 'posts/post_details.html'
    def get(self, request, *args, **kwargs):
        form = get_object_or_404(PostModel.objects.published(), pk=kwargs['post_id'], slug=kwargs['post_slug'])
        return render(request, self.template_name, {'form': form})
    