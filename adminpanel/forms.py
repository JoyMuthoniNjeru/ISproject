from django import forms
from .models import TestSlot
from testcentre.models import TestCentre
from django.forms.widgets import DateInput, TimeInput

class TestSlotForm(forms.ModelForm):
    class Meta:
        model = TestSlot
        fields = ['test_centre', 'date', 'start_time', 'end_time', 'max_applicants']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': TimeInput(attrs={'type': 'time'}),
            'end_time': TimeInput(attrs={'type': 'time'}),
}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter only test centres created by managers
        self.fields['test_centre'].queryset = TestCentre.objects.filter(manager__userprofile__user_type='manager')
