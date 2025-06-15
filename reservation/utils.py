
# Liste blanche des services autorisés
SERVICES_AUTORISES = [
    "Plomberie", "Électricité", "Ménage", "Jardinage", "Peinture", "Informatique", "Maçonnerie", "Menuiserie",
    "Serrurerie", "Déménagement", "Nettoyage", "Baby-sitting", "Coiffure", "Esthétique", "Photographie", "Cuisine",
    "Bricolage", "Réparation électroménager", "Réparation téléphone", "Réparation ordinateur", "Cours particuliers",
    "Traduction", "Rédaction", "Comptabilité", "Gestion administrative", "Livraison", "Chauffeur privé", "Taxi",
    "VTC", "Location voiture", "Location utilitaire", "Location matériel", "Sécurité", "Gardiennage", "Agent de sécurité",
    "Animation", "DJ", "Musicien", "Chanteur", "Organisation événement", "Décoration", "Fleuriste", "Pâtisserie",
    "Boulangerie", "Charcuterie", "Boucherie", "Poissonnerie", "Vente fruits et légumes", "Vente vêtements",
    "Vente chaussures", "Vente accessoires", "Vente téléphones", "Vente ordinateurs", "Vente meubles", "Vente électroménager",
    "Vente bijoux", "Vente montres", "Vente lunettes", "Vente produits beauté", "Vente produits ménagers", "Vente jouets",
    "Vente livres", "Vente fournitures scolaires", "Vente matériel informatique", "Vente matériel médical", "Vente pièces auto",
    "Vente motos", "Vente vélos", "Vente scooters", "Vente pièces détachées", "Vente matériaux construction", "Vente peinture",
    "Vente outils", "Vente équipements sportifs", "Vente instruments musique", "Vente plantes", "Vente graines", "Vente animaux",
    "Vente accessoires animaux", "Vente produits agricoles", "Vente produits artisanaux", "Vente produits locaux", "Vente souvenirs",
    "Vente objets déco", "Vente art", "Vente antiquités", "Vente vêtements enfants", "Vente vêtements femmes", "Vente vêtements hommes",
    "Vente sacs", "Vente valises", "Vente parapluies", "Vente chapeaux", "Vente ceintures", "Vente portefeuilles", "Vente bijoux fantaisie",
    "Vente produits électroniques", "Vente consoles jeux", "Vente jeux vidéo", "Vente accessoires jeux", "Vente télévisions",
    "Vente radios", "Vente appareils photo", "Vente caméras", "Vente drones", "Vente imprimantes", "Vente scanners", "Vente cartouches",
    "Vente fournitures bureau", "Vente mobilier bureau", "Vente lampes", "Vente ampoules", "Vente piles", "Vente batteries",
    "Vente chargeurs", "Vente câbles", "Vente adaptateurs", "Vente multiprises", "Vente rallonges", "Vente interrupteurs",
    "Vente prises", "Vente disjoncteurs", "Vente tableaux électriques", "Vente coffrets", "Vente alarmes", "Vente caméras surveillance",
    "Vente extincteurs", "Vente détecteurs fumée", "Vente serrures", "Vente cadenas", "Vente clés", "Vente portes", "Vente fenêtres",
    "Vente volets", "Vente stores", "Vente rideaux", "Vente tringles", "Vente tapis", "Vente moquettes", "Vente carrelage",
    "Vente faïence", "Vente parquet", "Vente lino", "Vente peinture murale", "Vente papier peint", "Vente colles", "Vente enduits",
    "Vente plâtre", "Vente ciment", "Vente sable", "Vente gravier", "Vente briques", "Vente parpaings", "Vente tuiles", "Vente ardoises",
    "Vente gouttières", "Vente chéneaux", "Vente descentes eaux", "Vente cuves", "Vente citernes", "Vente pompes", "Vente arrosage",
    "Vente tuyaux", "Vente robinets", "Vente lavabos", "Vente éviers", "Vente baignoires", "Vente douches", "Vente WC", "Vente broyeurs",
    "Vente fosses septiques", "Vente filtres", "Vente climatiseurs", "Vente ventilateurs", "Vente radiateurs", "Vente chaudières",
    "Vente poêles", "Vente cheminées", "Vente bois", "Vente granulés", "Vente charbon", "Vente gaz", "Vente fioul", "Vente panneaux solaires",
    "Vente éoliennes", "Vente batteries solaires", "Vente onduleurs", "Vente régulateurs", "Vente câbles solaires", "Vente prises solaires",
    "Vente piscines", "Vente spas", "Vente saunas", "Vente barbecues", "Vente abris de jardin",
    "Vente serres", "Vente panneaux clôture", "Vente portails", "Vente pergolas", "Vente fontaines"
]

# Fonction différée pour obtenir le modèle Notification
from django.apps import apps

def get_notification_model():
    return apps.get_model('reservation', 'Notification')

def notifier(utilisateur, message):
    Notification = get_notification_model()  # ✅ il faut l'appeler ici
    Notification.objects.create(utilisateur=utilisateur, message=message)


def initialiser_services_autorises():
    from reservation.models import Service
    for nom in SERVICES_AUTORISES:
        Service.objects.get_or_create(nom__iexact=nom, defaults={'nom': nom})