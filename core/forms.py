from django import forms
from core.models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPES)
