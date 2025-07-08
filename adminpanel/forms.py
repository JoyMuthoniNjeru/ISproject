from django import forms
from .models import TestSlot
from testcentre.models import TestCentre
from django.forms.widgets import DateInput, TimeInput
from django.core.exceptions import ValidationError

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

    def clean(self):
        cleaned_data = super().clean()
        centre = cleaned_data.get('test_centre')
        date = cleaned_data.get('date')
        new_applicants = cleaned_data.get('max_applicants')

        if centre and date and new_applicants is not None:
            existing_slots = TestSlot.objects.filter(test_centre=centre, date=date)
            total_applicants = sum(slot.max_applicants for slot in existing_slots)
            if total_applicants + new_applicants > centre.capacity:
                raise ValidationError(f"Total applicants exceed the capacity of {centre.capacity} for that day.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter only test centres created by managers
        self.fields['test_centre'].queryset = TestCentre.objects.filter(manager__userprofile__user_type='manager')
