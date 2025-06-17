from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.apps import apps

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, role='client'):
        if not email:
            raise ValueError('L’adresse email est obligatoire')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password, role='admin')
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Roles(models.TextChoices):
        CLIENT = 'client', _('Client')
        PRESTATAIRE = 'prestataire', _('Prestataire')

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='utilisateurs/photos/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.CLIENT)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f"{self.name} ({self.role})"

    @property
    def signalements(self):
        """Retourne les signalements liés à ce prestataire s’il en a un"""
        if hasattr(self, 'prestataire'):
            Signalement = apps.get_model('reservation', 'Signalement')
            return Signalement.objects.filter(prestataire=self.prestataire)
        return []

    class Meta:
        ordering = ['name']

class TypeContact(models.Model):
    nom = models.CharField(max_length=50)  # Ex: Téléphone, WhatsApp, Email

    def __str__(self):
        return self.nom

class ContactUtilisateur(models.Model):
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    type_contact = models.ForeignKey(TypeContact, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)  # Ex: le numéro ou l'email

    def __str__(self):
        return f"{self.utilisateur} - {self.type_contact.nom}: {self.contact}"


