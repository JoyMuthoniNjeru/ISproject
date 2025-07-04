from django import forms
from .models import Booking
from .models import Payment
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
    
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['booking']
        widgets = {
            'pin': forms.PasswordInput(),
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 1050:
            raise forms.ValidationError("Minimum payment is KES 1050.")
        return amount
