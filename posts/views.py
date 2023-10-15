from django.shortcuts import render
from django.views import View
from .models import Post


class HomeView(View):
    templated_name = 'posts/home.html'
    def get(self, request):
        all_post = Post.objects.filter(is_active=True).order_by('-created_at')[:10]
        return render(request, self.templated_name, {'home': all_post})


class DetailsPostHomeView(View):
    template_name = 'posts/post_details.html'
    def get(self, request, *args, **kwargs):
        form = Post.objects.get(pk=kwargs['post_id'], slug=kwargs['post_slug'])
        return render(request, self.template_name, {'form': form})