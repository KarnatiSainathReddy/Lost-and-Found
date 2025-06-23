from django import forms
from .models import LostFoundItem

class LostFoundItemForm(forms.ModelForm):
    class Meta:
        model = LostFoundItem
        exclude = ['posted_by', 'is_verified', 'date_reported']