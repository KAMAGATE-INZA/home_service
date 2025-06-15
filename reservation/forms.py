from django import forms
from .models import Reservation, Service, Avis, Prestataire, ServiceOffert, Message, Signalement
from django.contrib.auth import get_user_model
from .utils import SERVICES_AUTORISES
from accounts.models import CustomUser
from django.core.exceptions import ValidationError

User = get_user_model()

# Formulaire pour créer un prestataire
class PrestataireForm(forms.ModelForm):
    class Meta:
        model = Prestataire
        fields = ['zone', 'photo']
        widgets = {
            'zone': forms.TextInput(attrs={
                'class': 'search-input',
                'placeholder': 'Zone d’intervention'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'search-input'
            }),
        }

# Formulaire pour réserver un service
class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    heure = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))

    class Meta:
        model = Reservation
        fields = ['date', 'heure', 'mode_paiement']
        widgets = {
            'mode_paiement': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if not self.fields[field].widget.attrs.get('class'):
                self.fields[field].widget.attrs['class'] = 'form-control'

# Formulaire pour créer un service
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulaire pour créer une offre de service
class ServiceOffertForm(forms.ModelForm):
    class Meta:
        model = ServiceOffert
        fields = ['service', 'prix', 'description']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Formulaire pour choisir un service existant
class AjouterServiceExistForm(forms.Form):
    service = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        label="Choisir un service existant",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

# Formulaire pour créer un nouveau service
class NouveauServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulaire pour laisser un avis
class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['note', 'commentaire']
        widgets = {
            'note': forms.NumberInput(attrs={'class': 'form-control'}),
            'commentaire': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Remplacer ServiceDatalistForm par :
class ServiceDatalistForm(forms.ModelForm):
    service = forms.CharField(
        label="Nom du service",
        widget=forms.TextInput(attrs={
            'list': 'services-list',
            'class': 'form-control',
            'placeholder': 'Choisissez un service autorisé'
        })
    )

    class Meta:
        model = ServiceOffert
        fields = ['service', 'prix', 'description']
        widgets = {
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.prestataire = kwargs.pop('prestataire', None)
        super().__init__(*args, **kwargs)

    def clean_service(self):
        nom = self.cleaned_data['service'].strip()
        if nom not in SERVICES_AUTORISES:
            raise ValidationError("Ce service n'est pas reconnu.")

        # Récupère ou crée le service
        service, _ = Service.objects.get_or_create(nom__iexact=nom, defaults={'nom': nom})

        # Vérifie s'il est déjà proposé par ce prestataire
        if self.prestataire and ServiceOffert.objects.filter(service=service, prestataire=self.prestataire).exists():
            raise ValidationError("Ce service est déjà proposé par vous.")

        return service
    
# Formulaire pour reporter une réservation
class ReporterReservationForm(forms.Form):
    nouvelle_date = forms.DateField(label="Nouvelle date", widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    nouvelle_heure = forms.TimeField(label="Nouvelle heure", widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))

# Formulaire pour les messages
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']  # ✅ on ne met PAS 'recipient'
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class MessageReservationForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'reservation']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'reservation': forms.HiddenInput(),  # utile pour la vue
        }

# Formulaire pour les utilisateurs
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'photo']  # ✅ Ajoute "photo"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# Formulaire pour les signalements
class SignalementForm(forms.ModelForm):
    class Meta:
        model = Signalement
        fields = ['motif', 'description', 'preuve']
        widgets = {
            'motif': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'preuve': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


