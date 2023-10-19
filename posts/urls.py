from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('details/<int:post_id>/<slug:post_slug>/', views.DetailsPostHomeView.as_view(),
         name='details_post'),
]
