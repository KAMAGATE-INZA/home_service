from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .utils import SERVICES_AUTORISES

# 🔹 Modèle Service (plomberie, coiffure, etc.)
class Service(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nom']

    def __str__(self):
        return self.nom


# 🔹 Prestataire de services
class Prestataire(models.Model):
    utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='prestataires/photos/', blank=True, null=True)
    evaluation_moyenne = models.FloatField(default=0.0)

    class Meta:
        ordering = ['utilisateur__name']

    def __str__(self):
        return f"{self.utilisateur.name} ({self.zone})"


# 🔹 Offre d’un service par un prestataire avec prix personnalisé
class ServiceOffert(models.Model):
    prestataire = models.ForeignKey(Prestataire, on_delete=models.CASCADE, related_name='offres')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='offres')
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    class Meta:
        unique_together = ('prestataire', 'service')
        ordering = ['service__nom']

    def __str__(self):
        return f"{self.service.nom} - {self.prestataire.utilisateur.name}"

    def clean(self):
        super().clean()
        if hasattr(self, 'service') and self.service.nom not in SERVICES_AUTORISES:
            raise ValidationError(
                {'service': f"Le service '{self.service.nom}' n'est pas autorisé."}
            )


# 🔹 Réservation faite par un client
class Reservation(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
    service_offert = models.ForeignKey(ServiceOffert, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()
    nouvelle_date = models.DateField(null=True, blank=True)
    nouvelle_heure = models.TimeField(null=True, blank=True)

    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('acceptée', 'Acceptée'),
        ('refusée', 'Refusée'),
        ('terminée', 'Terminée'),
        ('date_passée', 'Date passée'),
        ('annulée', 'Annulée'),
        ('en_attente_confirmation', 'En attente de confirmation'),
        ('reportée', 'Reportée'),
    ]
    statut = models.CharField(max_length=60, choices=STATUT_CHOICES, default='en_attente')
    mode_paiement = models.CharField(max_length=30, blank=True)
    report_en_attente = models.BooleanField(default=False)
    reporteur = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='reservations_reportees'
    )

    class Meta:
        ordering = ['-date', '-heure']

    def __str__(self):
        return f"{self.client.name} → {self.service_offert} ({self.get_statut_display()})"

    def get_statut_display_label(self):
        return dict(self.STATUT_CHOICES).get(self.statut, self.statut)


# 🔹 Avis client
class Avis(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='avis_laisses')
    prestataire = models.ForeignKey(Prestataire, on_delete=models.CASCADE, related_name='avis_recus')
    commentaire = models.TextField()
    note = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('client', 'prestataire')
        ordering = ['-date']

    def __str__(self):
        return f"{self.client.name} → {self.prestataire.utilisateur.name} : {self.note}/5"


# 🔹 Notifications
class Notification(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)
    auto = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"🔔 {self.utilisateur.name} : {self.message}"


# 🔹 Message privé (ou lié à un signalement)
class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages_envoyes')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages_recus')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    signalement = models.ForeignKey('Signalement', on_delete=models.CASCADE, null=True, blank=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"De {self.sender.name} à {self.recipient.name}"


# 🔹 Signalement d’un prestataire
class Signalement(models.Model):
    prestataire = models.ForeignKey('Prestataire', on_delete=models.CASCADE, related_name='signalements')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='signalements_faits')
    motif = models.CharField(max_length=255)
    description = models.TextField()
    preuve = models.FileField(upload_to='preuves_signalement/', blank=True, null=True)
    date_signalement = models.DateTimeField(auto_now_add=True)
    traite = models.BooleanField(default=False)
    defense = models.TextField(blank=True, null=True)
    preuve_defense = models.FileField(upload_to='preuves_defense/', blank=True, null=True)
    statut = models.CharField(
        max_length=20,
        choices=[('en_attente', 'En attente'), ('averti', 'Averti'), ('banni', 'Banni')],
        default='en_attente'
    )

    class Meta:
        ordering = ['-date_signalement']

    def __str__(self):
        return f"{self.client.name} signale {self.prestataire.utilisateur.name}"


# 🔹 Liste des prestataires bannis
class PrestataireBanni(models.Model):
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=30)
    nom = models.CharField(max_length=255)
    date_bannissement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} (banni)"


# 🔹 Abonnement à la newsletter
class NewsletterEmail(models.Model):
    email = models.EmailField(unique=True)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
