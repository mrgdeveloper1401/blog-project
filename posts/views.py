from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import PostModel, CategoryModel
from django.core.paginator import Paginator
from tickets.form import feedbackForm
from django.contrib import messages


class HomeView(View):
    templated_name = 'posts/home.html'
    form_class = feedbackForm
    def get(self, request):
        form = self.form_class()
        all_post = PostModel.published.order_by('-created_at')[:10]
        category = CategoryModel.objects.all()
        
        paginator = Paginator(all_post, 1)
        page_number = request.GET.get('page')
        all_post = paginator.get_page(page_number)
        
        context = {
            'post': all_post,
            'category': category,
            'form': form,
        }
        return render(request, self.templated_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            first_name = cd['first_name']
            last_name = cd['last_name']
            email = cd['email']
            body = cd['body']
            form.save()
            messages.success(request, 'Thanks for your feedback!')
            return redirect('posts:home')
        return render(request, self.templated_name, {'form': form})


class DetailsPostHomeView(View):
    template_name = 'posts/post_details.html'
    def get(self, request, *args, **kwargs):
        form = get_object_or_404(PostModel.published, pk=kwargs['post_id'], slug=kwargs['post_slug'])
        return render(request, self.template_name, {'form': form})
    