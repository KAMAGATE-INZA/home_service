from django.urls import path
from . import views
from .views import (
    completer_profil_prestataire, mes_services, modifier_service, supprimer_service,
    service_detail, mes_reservations, action_reservation,mes_signalements
)

urlpatterns = [
    path('', views.home_view, name='home'),
    path('services/<int:service_id>/reserver/', views.reserver_service, name='reserver_service'),
    path('prestataire/<int:prestataire_id>/avis/', views.laisser_avis, name='laisser_avis'),
    path('prestataire/completer-profil/', completer_profil_prestataire, name='completer_profil_prestataire'),
    path('prestataire/mes-services/', mes_services, name='mes_services'),
    path('prestataire/modifier-service/<int:service_id>/', modifier_service, name='modifier_service'),
    path('prestataire/supprimer-service/<int:service_id>/', supprimer_service, name='supprimer_service'),
    path('prestataire/ajouter-service/', views.ajouter_service_offert, name='ajouter_service_offert'),  # Ajout de la bonne vue
    path('services/<int:service_id>/', service_detail, name='service_detail'),
    path('mes-reservations/', mes_reservations, name='mes_reservations'),
    path('prestataire/mes-reservations/', views.mes_reservations_prestataire, name='mes_reservations_prestataire'),
    path('prestataire/reservation/<int:reservation_id>/<str:action>/', action_reservation, name='action_reservation'),
    path('reservation/marquer-terminee/<int:reservation_id>/<str:statut>/', views.changer_statut_reservation, name='changer_statut_reservation'),
    path('reservation/<int:reservation_id>/<str:action>_client/', views.action_reservation_client, name='action_reservation_client'),
    path('reservation/<int:reservation_id>/reporter/', views.reporter_reservation, name='reporter_reservation'),
    path('reservation/<int:reservation_id>/confirmer-report/', views.confirmer_report, name='confirmer_report'),
    path('reservation/<int:reservation_id>/refuser-report/', views.refuser_report, name='refuser_report'),
    path('prestataire/<int:prestataire_id>/', views.detail_prestataire, name='detail_prestataire'),
    path('communaute/', views.communaute, name='communaute'),
    path('prestataires/', views.page_prestataire, name='page_prestataire'),
    path('services/', views.page_services, name='page_services'),
    path('temoignages/', views.page_temoignages, name='page_temoignages'),
    path('notification/lue/<int:notification_id>/', views.marquer_notification_lue, name='marquer_notification_lue'),
    path('notifications/historique/', views.historique_notifications, name='historique_notifications'),
    path('notifications/tout-lu/', views.marquer_tout_lu, name='marquer_tout_lu'),
    path('notifications/supprimer/<int:notification_id>/', views.supprimer_notification, name='supprimer_notification'),
    path('notifications/tout-supprimer/', views.supprimer_toutes_notifications, name='supprimer_toutes_notifications'),
    path('messages/', views.boite_reception, name='boite_reception'),
    path('messages/envoyer/', views.envoyer_message, name='envoyer_message'),
    # Pour afficher les messages liés à une réservation :
    path('messages/reservation/<int:reservation_id>/', views.messages_reservation, name='messages_reservation'),
    path('messages/supprimer/<int:message_id>/', views.supprimer_message, name='supprimer_message'),
    path('profil/modifier/', views.modifier_profil, name='modifier_profil'),
    path('profil/supprimer/', views.supprimer_profil, name='supprimer_profil'),
    path('prestataire/<int:prestataire_id>/signaler/', views.signaler_prestataire, name='signaler_prestataire'),
    path('signalement/<int:signalement_id>/defense/', views.defense_signalement, name='defense_signalement'),
    path('signalement/<int:signalement_id>/avertir/', views.avertir_prestataire, name='avertir_prestataire'),
    path('signalement/<int:signalement_id>/bannir/', views.bannir_prestataire, name='bannir_prestataire'),
    path('dashboard-admin/', views.dashboard_admin, name='dashboard_admin'),
    path('messages/prestataire/<int:prestataire_id>/', views.messages_admin_prestataire, name='messages_admin_prestataire'),
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('mes_signalements/', views.mes_signalements, name='mes_signalements'),
path('boite-prestataire/', views.boite_reception_prestataire, name='boite_reception_prestataire'),

]
