from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'primary_use']
        widgets = {
            'full_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'primary_use': forms.Select(),
        }
