from reservation.models import Service
from .utils import SERVICES_AUTORISES

def initialiser_services_autorises():
    for nom in SERVICES_AUTORISES:
        Service.objects.get_or_create(nom__iexact=nom.strip(), defaults={'nom': nom.strip()})