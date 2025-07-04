from django import forms
from .models import Booking
import os
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user', 'confirmed']
        widgets = {
            'gender': forms.Select(choices=[('female', 'Female'), ('male', 'Male'), ('prefer not to say', 'Prefer not to say')]),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'test_slot': forms.Select(),
        }

    def clean_document_upload(self):
        file = self.cleaned_data.get('document_upload', False)

        if file:
            ext = os.path.splitext(file.name)[1].lower()
            valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp']
            if ext not in valid_extensions:
                raise ValidationError("Unsupported file type. Please upload an image file.")
        return file
