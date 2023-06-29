from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=(('customer', 'Customer'), ('worker', 'Technical Worker'), ('management', 'Senior Management')))
    name = forms.CharField(max_length=255)