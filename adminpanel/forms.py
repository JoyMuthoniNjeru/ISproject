from django import forms
from .models import TestSlot
from testcentre.models import TestCentre
from django.forms.widgets import DateInput, TimeInput

class TestSlotForm(forms.ModelForm):
    class Meta:
        model = TestSlot
        fields = ['test_centre', 'date', 'time_range', 'max_applicants']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time_range': forms.TextInput(attrs={
                'placeholder': 'e.g. 08:00 AM – 10:00 AM',
                'class': 'form-control',
            }),
            'max_applicants': forms.NumberInput(attrs={'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter only test centres created by managers
        self.fields['test_centre'].queryset = TestCentre.objects.filter(manager__userprofile__user_type='manager')
