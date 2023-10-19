from django.shortcuts import render, redirect
from .forms import SignUpMobileForm, SignUpEmailForm
from django.views import View

class SingUpview(View):
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
    

class SingInView(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass