from reservation.models import Service

services = [
    "Plomberie", "Électricité", "Ménage", "Repassage", "Jardinage", "Coiffure", "Esthétique", "Massage",
    "Garde d’enfants", "Soutien scolaire", "Informatique", "Réparation électroménager", "Peinture", "Déménagement",
    "Montage de meubles", "Couture", "Babysitting", "Cours de musique", "Cours de sport", "Cours de cuisine",
    "Livraison de courses", "Assistance administrative", "Nettoyage de vitres", "Nettoyage de tapis", "Entretien piscine",
    "Désinsectisation", "Dératisation", "Débarras", "Petits travaux", "Serrurerie", "Chauffage", "Climatisation",
    "Photographie", "Vidéaste", "Coach sportif", "Diététicien", "Nutritionniste", "Sophrologue", "Psychologue",
    "Orthophoniste", "Ergothérapeute", "Ostéopathe", "Kinésithérapeute", "Infirmier à domicile", "Aide aux personnes âgées",
    "Aide aux personnes handicapées", "Promenade d’animaux", "Toilettage d’animaux", "Dressage d’animaux", "Garde d’animaux",
    "Installation alarme", "Installation domotique", "Réparation smartphone", "Réparation ordinateur", "Dépannage internet",
    "Installation TV", "Installation parabole", "Nettoyage voiture", "Entretien moto", "Réparation vélo", "Livraison repas",
    "Chef à domicile", "Pâtissier à domicile", "Traiteur", "Organisation d’événements", "DJ à domicile", "Animation enfants",
    "Magicien à domicile", "Clown à domicile", "Décoration intérieure", "Architecte d’intérieur", "Conseiller en image",
    "Personal shopper", "Styliste", "Manucure", "Pédicure", "Maquillage", "Epilation", "Bronzage", "Massage bébé",
    "Réflexologue", "Acupuncteur", "Professeur de yoga", "Professeur de danse", "Professeur de langues", "Traducteur",
    "Interprète", "Rédacteur", "Correcteur", "Graphiste", "Webdesigner", "Développeur web", "Community manager",
    "Assistant virtuel", "Conseiller fiscal", "Conseiller juridique", "Courtier en assurance", "Courtier immobilier",
    "Agent de sécurité", "Chauffeur privé"
]

for nom in services:
    Service.objects.get_or_create(nom=nom)
print("Import terminé !")