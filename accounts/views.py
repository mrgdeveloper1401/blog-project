from django.shortcuts import render, redirect
from .forms import SignUpMobileForm, SignUpEmailForm, LoginEmailForm, LoginMobileForm
from django.views import View

class SingUpMobileview(View):
    form_class = SignUpMobileForm
    template_name = 'accounts/signup-mobile.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        pass
    

class SingUpEmailview(View):
    template_name = 'accounts/signup-email.html'
    form_class = SignUpEmailForm
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        pass
    

class SingInMobileView(View):
    form_class = LoginMobileForm
    template_name = 'accounts/login-mobile.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        pass
    
    
class SignInEmailView(View):
    form_class = LoginEmailForm
    template_name = 'accounts/login-email.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        pass