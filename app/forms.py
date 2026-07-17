from django import forms
from app.models import Registration

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="Confirm Password", 
        max_length=25, 
        required=True
        )
    class Meta:
        model = Registration
        fields = ('first_name', 'last_name', 'email_address', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
