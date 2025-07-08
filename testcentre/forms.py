from django import forms
from .models import TestCentre

class TestCentreForm(forms.ModelForm):
    class Meta:
        model = TestCentre
        fields = ['name', 'location', 'capacity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),  
        }
