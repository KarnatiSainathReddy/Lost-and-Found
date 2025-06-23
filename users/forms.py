from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'image': forms.FileInput(),
            'displayname': forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Add phone number'}),
            'address': forms.TextInput(attrs={'placeholder': 'Add address'}),
            'city': forms.TextInput(attrs={'placeholder': 'Add city'}),
            'country': forms.TextInput(attrs={'placeholder': 'Add country'}),
        }


class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']