from django import forms
from .models import Users


class SignUpMobileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('mobile_phone', )
        

class SignUpEmailForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('email', )
        
        
class LoginEmailForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('email', 'password')
        

class LoginMobileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('mobile_phone', 'password')