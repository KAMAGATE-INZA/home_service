from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.models import Q
from reservation.models import Reservation, Notification

class Command(BaseCommand):
    help = "Marque automatiquement comme terminées les réservations dont la date et l'heure sont passées, non reportées et non terminées, et notifie client et prestataire."

    def handle(self, *args, **kwargs):
        now = timezone.localtime()
        today = now.date()
        current_time = now.time()

        reservations = Reservation.objects.filter(
            statut__in=['en_attente', 'acceptée'],
            nouvelle_date__isnull=True
        ).filter(
            Q(date__lt=today) | Q(date=today, heure__lt=current_time)
        )

        count = 0
        for r in reservations:
            r.statut = 'terminée'
            r.save()
            # Notification au client
            Notification.objects.create(
                utilisateur=r.client,
                message=f"Votre réservation du {r.date} à {r.heure} pour le service {r.service_offert.service.nom} a été automatiquement marquée comme terminée.",
                auto=True
            )
            # Notification au prestataire
            Notification.objects.create(
                utilisateur=r.service_offert.prestataire.utilisateur,
                message=f"La réservation du {r.date} à {r.heure} pour votre service {r.service_offert.service.nom} a été automatiquement marquée comme terminée."
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f"{count} réservations marquées comme terminées et notifications envoyées."))