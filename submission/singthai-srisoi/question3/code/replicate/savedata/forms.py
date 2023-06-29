from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
        }