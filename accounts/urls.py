from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup-mobile/', views.SingInMobileView.as_view(), name='signup-mobile'),
    path('signup-email/', views.SingUpEmailview.as_view(), name='signup-email'),
    path('signin-email/', views.SingUpEmailview.as_view(), name='signin-email'),
    path('signin-mobile/', views.SingInMobileView.as_view(), name='signin-mobile'),
    
]