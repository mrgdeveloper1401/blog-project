from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SingUpview.as_view(), name='signup-mobile'),
    path('signin/', views.SingUpview.as_view(), name='signin'),
    path('signup-email/', views.SingUpEmailview.as_view(), name='signupEmail'),
    
]