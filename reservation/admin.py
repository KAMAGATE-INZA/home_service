from django.contrib import admin
from .models import Service, Prestataire, Reservation, Avis, ServiceOffert
from django.apps import apps
Notification = apps.get_model('reservation', 'Notification')

admin.site.register(Service)
admin.site.register(Prestataire)
admin.site.register(Reservation)
admin.site.register(Avis)
admin.site.register(ServiceOffert)
admin.site.register(Notification)