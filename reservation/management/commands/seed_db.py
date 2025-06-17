import random
from datetime import timedelta, time
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from accounts.models import TypeContact, ContactUtilisateur
from reservation.models import (
    Service, ServiceOffert, Reservation, Avis,
    Prestataire, Message, Signalement
)
from reservation.utils import SERVICES_AUTORISES

User = get_user_model()

descriptions_possibles = [
    "Service professionnel de {service} proposé par {prestataire}",
    "Besoin de {service} ? {prestataire} est à votre service !",
    "{prestataire} assure un travail soigné en {service}",
    "Faites confiance à {prestataire} pour vos besoins en {service}",
    "Expert en {service}, {prestataire} est là pour vous aider",
    "{prestataire} : la référence en matière de {service}",
    "{service} rapide et efficace assuré par {prestataire}",
    "Un service de qualité en {service} avec {prestataire}",
    "{prestataire} est votre spécialiste du {service}",
    "{service} sur mesure avec {prestataire}",
]

class Command(BaseCommand):
    help = "Supprime les anciennes données et préremplit la base avec des données de test."

    def handle(self, *args, **kwargs):
        self.stdout.write("⚠️ Suppression des anciennes données...")

        # Suppression dans l'ordre
        Message.objects.all().delete()
        Avis.objects.all().delete()
        Reservation.objects.all().delete()
        Signalement.objects.all().delete()
        ServiceOffert.objects.all().delete()
        Service.objects.all().delete()
        ContactUtilisateur.objects.all().delete()
        Prestataire.objects.all().delete()
        TypeContact.objects.all().delete()
        User.objects.filter(role__in=["client", "prestataire"]).delete()

        self.stdout.write("✅ Données supprimées.")

        # Types de contact
        types_contacts = ["Téléphone", "Email", "Facebook", "WhatsApp"]
        type_objs = [TypeContact.objects.create(nom=t) for t in types_contacts]

        # Clients
        clients = []
        for i in range(1, 51):
            client = User.objects.create_user(
                name=f"Client{i}",
                email=f"client{i}@example.com",
                password="test1234",
                role="client"
            )
            clients.append(client)

        # Prestataires
        prestataires = []
        zones = ["Abidjan", "Bouaké", "Yamoussoukro", "San Pedro"]
        for i in range(1, 51):
            user = User.objects.create_user(
                name=f"Prestataire{i}",
                email=f"prestataire{i}@example.com",
                password="test1234",
                role="prestataire"
            )
            prestataire = Prestataire.objects.create(
                utilisateur=user,
                zone=random.choice(zones),
                evaluation_moyenne=round(random.uniform(3.0, 5.0), 1)
            )
            prestataires.append(prestataire)

        # Contacts
        for user in clients + [p.utilisateur for p in prestataires]:
            ContactUtilisateur.objects.create(
                utilisateur=user,
                type_contact=random.choice(type_objs),
                contact=f"07{random.randint(10000000, 99999999)}"
            )

        # Services
        services_objs = []
        noms_choisis = random.sample(SERVICES_AUTORISES, 50)
        for nom in noms_choisis:
            service, _ = Service.objects.get_or_create(nom=nom)
            services_objs.append(service)

        self.stdout.write("✅ 50 services créés.")

        # Services offerts
        for prestataire in prestataires:
            services_selectionnes = random.sample(services_objs, random.randint(3, 5))
            for service in services_selectionnes:
                description = random.choice(descriptions_possibles).format(
                    service=service.nom.lower(),
                    prestataire=prestataire.utilisateur.name
                )
                ServiceOffert.objects.create(
                    service=service,
                    prestataire=prestataire,
                    prix=random.randint(5000, 20000),
                    description=description
                )

        # Réservations sans doublon
        self.stdout.write("📅 Création de réservations...")
        all_service_offerts = list(ServiceOffert.objects.all())
        used_combinations = set()
        reservations = []

        while len(reservations) < 100:
            client = random.choice(clients)
            service_offert = random.choice(all_service_offerts)
            date_obj = timezone.now().date() + timedelta(days=random.randint(0, 30))
            heure_obj = time(hour=random.randint(8, 18))

            key = (client.id, service_offert.id, date_obj, heure_obj)

            if key not in used_combinations:
                used_combinations.add(key)
                reservation = Reservation.objects.create(
                    client=client,
                    service_offert=service_offert,
                    date=date_obj,
                    heure=heure_obj,
                    statut=random.choice([s[0] for s in Reservation.STATUT_CHOICES]),
                    mode_paiement=random.choice(["espèces", "carte", "mobile money"])
                )
                reservations.append(reservation)

        self.stdout.write(self.style.SUCCESS(f"✅ {len(reservations)} réservations créées."))

        # Avis
        self.stdout.write("✍️ Création des avis...")
        avis_crees = set()
        tentatives = 0

        while len(avis_crees) < 50 and tentatives < 500:
            client = random.choice(clients)
            prestataire = random.choice(prestataires)
            key = (client.id, prestataire.id)

            if key not in avis_crees:
                Avis.objects.create(
                    client=client,
                    prestataire=prestataire,
                    note=random.randint(1, 5),
                    commentaire="Avis généré automatiquement."
                )
                avis_crees.add(key)
            else:
                tentatives += 1

        self.stdout.write(self.style.SUCCESS(f"✅ {len(avis_crees)} avis créés."))

        # Messages
        self.stdout.write("💬 Création des messages...")
        for reservation in random.sample(reservations, 30):
            Message.objects.create(
                sender=reservation.client,
                recipient=reservation.service_offert.prestataire.utilisateur,
                content="Bonjour, j’ai une question concernant la réservation.",
                reservation=reservation
            )
        self.stdout.write(self.style.SUCCESS("✅ 30 messages créés."))

        # Signalements
        self.stdout.write("🚨 Création de signalements...")
        for _ in range(10):
            client = random.choice(clients)
            prestataire = random.choice(prestataires)
            Signalement.objects.create(
                client=client,
                prestataire=prestataire,
                motif="Comportement inapproprié",
                description="Le prestataire est arrivé en retard sans prévenir.",
                statut=random.choice(['en_attente', 'averti', 'banni'])
            )
        self.stdout.write(self.style.SUCCESS("✅ 10 signalements créés."))

        self.stdout.write(self.style.SUCCESS("🎉 Base de données de test prête !"))
