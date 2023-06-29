from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('technical', 'Technical Worker'),
        ('management', 'Senior Management'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPES)

    class Meta:
        model = User
        fields = ('username', 'email', 'user_type', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)