from django import forms
from .models import TicketMoel


class feedbackForm(forms.ModelForm):
    class Meta:
        model = TicketMoel
        fields = '__all__'