import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.models import TypeContact, ContactUtilisateur
from reservation.models import Service, ServiceOffert, Reservation, Avis
from django.utils import timezone
from datetime import timedelta
from reservation.models import Prestataire
from reservation.utils import SERVICES_AUTORISES



User = get_user_model()

class Command(BaseCommand):
    help = "Supprime les anciennes données et préremplit la base avec des données de test."

    def handle(self, *args, **kwargs):
        self.stdout.write("⚠️ Suppression des anciennes données...")

        # Supprimer les données dans l'ordre pour respecter les FK
        Avis.objects.all().delete()
        Reservation.objects.all().delete()
        ServiceOffert.objects.all().delete()
        Service.objects.all().delete()
        ContactUtilisateur.objects.all().delete()
        Prestataire.objects.all().delete()
        TypeContact.objects.all().delete()
        User.objects.filter(role__in=["client", "prestataire"]).delete()

        self.stdout.write("✅ Données supprimées.")

        # Création des données
        self.stdout.write("🛠️ Création des données de test...")

        # Créer les types de contacts
        types_contacts = ["Téléphone", "Email", "Facebook", "WhatsApp"]
        type_objs = []
        for t in types_contacts:
            type_obj, _ = TypeContact.objects.get_or_create(nom=t)
            type_objs.append(type_obj)

        # Créer 50 clients
        clients = []
        for i in range(1, 51):
            client = User.objects.create_user(
                name=f"Client{i}",
                email=f"client{i}@example.com",
                password="test1234",
                role="client"
            )
            clients.append(client)

        # Créer 50 prestataires avec utilisateur associé
        prestataires = []
        zones = ["Abidjan", "Bouaké", "Yamoussoukro", "San Pedro"]
        for i in range(1, 51):
            prestataire_user = User.objects.create_user(
                name=f"Prestataire{i}",
                email=f"prestataire{i}@example.com",
                password="test1234",
                role="prestataire"
            )
            prestataire = Prestataire.objects.create(
                utilisateur=prestataire_user,
                zone=random.choice(zones),
                evaluation_moyenne=round(random.uniform(3.0, 5.0), 1)
            )
            prestataires.append(prestataire)

        # Ajouter des contacts aléatoires pour clients et prestataires
        for client in clients:
            ContactUtilisateur.objects.create(
                utilisateur=client,
                type_contact=random.choice(type_objs),
                contact=f"0600{random.randint(100000,999999)}"
            )
        for prestataire in prestataires:
            ContactUtilisateur.objects.create(
                utilisateur=prestataire.utilisateur,
                type_contact=random.choice(type_objs),
                contact=f"0700{random.randint(100000,999999)}"
            )

        services_objs = []

# Choisir 50 noms uniques au hasard parmi les services autorisés
        noms_choisis = random.sample(SERVICES_AUTORISES, 50)

        for nom in noms_choisis:
            service, created = Service.objects.get_or_create(
                nom=nom,
            )
            services_objs.append(service)

        print("✅ 50 services créés avec succès.")

        # Lier des services aux prestataires (3 à 5 services aléatoires chacun)
        for prestataire in prestataires:
            offered_services = random.sample(services_objs, random.randint(3, 5))
            for service in offered_services:
                ServiceOffert.objects.create(
                    service=service,
                    prestataire=prestataire,
                    prix=random.randint(5000, 20000)
                )

        # Créer 100 réservations
        all_service_offerts = ServiceOffert.objects.all()
        for _ in range(100):
            client = random.choice(clients)
            service_offert = random.choice(all_service_offerts)
            Reservation.objects.create(
                client=client,
                service_offert=service_offert,
                date=timezone.now().date() + timedelta(days=random.randint(0, 30)),
                heure=f"{random.randint(8, 18)}:00",
                statut=random.choice(["en attente", "confirmée", "terminée"]),
                mode_paiement=random.choice(["espèces", "carte", "mobile money"])
            )

        # Créer 50 avis
        for _ in range(50):
            client = random.choice(clients)
            prestataire = random.choice(prestataires)
            Avis.objects.create(
                client=client,
                prestataire=prestataire,
                note=random.randint(1, 5),
                commentaire="Avis généré automatiquement."
            )

        self.stdout.write(self.style.SUCCESS("✅ Base de données préremplie avec succès !"))
