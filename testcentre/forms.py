from django import forms
from .models import TestCentre

class TestCentreForm(forms.ModelForm):
    class Meta:
        model = TestCentre
        fields = ['name', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
