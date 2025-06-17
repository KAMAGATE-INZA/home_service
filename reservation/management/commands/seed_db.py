import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.models import TypeContact, ContactUtilisateur
from reservation.models import Service, ServiceOffert, Reservation, Avis, Prestataire
from django.utils import timezone
from datetime import timedelta
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

        # Création des types de contact
        types_contacts = ["Téléphone", "Email", "Facebook", "WhatsApp"]
        type_objs = []
        for t in types_contacts:
            type_obj, _ = TypeContact.objects.get_or_create(nom=t)
            type_objs.append(type_obj)

        # Création des clients
        clients = []
        for i in range(1, 51):
            client = User.objects.create_user(
                name=f"Client{i}",
                email=f"client{i}@example.com",
                password="test1234",
                role="client"
            )
            clients.append(client)

        # Création des prestataires
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

        # Ajouter contacts utilisateurs
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

        # Créer les services
        services_objs = []
        noms_choisis = random.sample(SERVICES_AUTORISES, 50)
        for nom in noms_choisis:
            service, _ = Service.objects.get_or_create(nom=nom)
            services_objs.append(service)

        self.stdout.write("✅ 50 services créés.")

        # Associer services offerts aux prestataires avec descriptions
        for prestataire in prestataires:
            services_selectionnes = random.sample(services_objs, random.randint(3, 5))
            for service in services_selectionnes:
                template = random.choice(descriptions_possibles)
                description = template.format(
                    service=service.nom.lower(),
                    prestataire=prestataire.utilisateur.name
                )
                ServiceOffert.objects.create(
                    service=service,
                    prestataire=prestataire,
                    prix=random.randint(5000, 20000),
                    description=description
                )

        # Créer les réservations
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

        # Créer les avis
        # Créer 50 avis sans doublon (client, prestataire)
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

        self.stdout.write(self.style.SUCCESS("✅ Base de données préremplie avec succès !"))
