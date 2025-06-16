from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, ContactUtilisateur, TypeContact

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'role', 'password1', 'password2']
        labels = {
            'email': "Adresse email",
            'name': "Nom complet",
            'role': "Rôle",
            'password1': "Mot de passe",
            'password2': "Confirmation du mot de passe",
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in self.Meta.widgets:
                self.fields[field].widget.attrs['class'] = 'form-control'

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Adresse email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

TYPE_CHOICES = [
    ('Téléphone', 'Téléphone'),
    ('Facebook', 'Facebook'),
    ('WhatsApp', 'WhatsApp'),
    ('Email', 'Email'),
    ('Autre', 'Préciser'),
]

class ContactUtilisateurForm(forms.ModelForm):
    class Meta:
        model = ContactUtilisateur
        fields = ['type_contact', 'contact']
        widgets = {
            'type_contact': forms.Select(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        if self.instance.pk and not str(self.instance.pk).isdigit():
            raise forms.ValidationError("L'identifiant est invalide.")
        return cleaned_data
