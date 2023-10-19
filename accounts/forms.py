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