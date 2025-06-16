from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, Prestataire, Reservation, Avis, ServiceOffert, Message, Signalement, PrestataireBanni, NewsletterEmail
from .forms import ReservationForm, ServiceForm, AvisForm, ServiceOffertForm, MessageForm, SignalementForm
from .forms import ServiceDatalistForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Count, Avg
from .forms import PrestataireForm, UserForm
from .models import Prestataire
from .forms import AjouterServiceExistForm, NouveauServiceForm
from django.db import models
from .utils import notifier, SERVICES_AUTORISES
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.db.models import Q
from .forms import ReporterReservationForm
from django.apps import apps
Notification = apps.get_model('reservation', 'Notification')


# reserver un service
@login_required
def reserver_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    # Vérifie que l'utilisateur est un client
    if request.user.role != 'client':
        messages.error(request, "Seuls les clients peuvent réserver un service.")
        return redirect('dashboard')

    # Récupère l'ID du prestataire depuis les paramètres GET
    prestataire_id = request.GET.get('prestataire')
    prestataire = get_object_or_404(Prestataire, pk=prestataire_id)

    # Vérifie que ce prestataire propose bien ce service via ServiceOffert
    try:
        service_offert = ServiceOffert.objects.get(prestataire=prestataire, service=service)
    except ServiceOffert.DoesNotExist:
        messages.error(request, "Ce prestataire ne propose pas ce service.")
        return redirect('home')

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            heure = form.cleaned_data['heure']
            # Vérification de l'unicité
            conflit = Reservation.objects.filter(
                service_offert=service_offert,
                date=date,
                heure=heure,
                statut__in=['en_attente', 'acceptée']
            ).exists()
            if conflit:
                messages.error(request, "Ce créneau est déjà réservé pour ce prestataire et ce service.")
            else:
                reservation = form.save(commit=False)
                reservation.client = request.user
                reservation.service_offert = service_offert
                reservation.statut = 'en_attente'
                reservation.save()
                messages.success(request, "Votre réservation a été effectuée avec succès.")
                # Notification au prestataire
                notifier(
                    service_offert.prestataire.utilisateur,
                    f"Nouvelle demande de réservation pour votre service {service_offert.service.nom}."
                )
                return redirect('mes_reservations')
    else:
        form = ReservationForm()

    return render(request, 'reservation/reserver_service.html', {
        'form': form,
        'service': service,
        'prestataire': prestataire,
        'service_offert': service_offert,
    })

@login_required
def mes_reservations(request):
    if request.user.role != 'client':
        return redirect('dashboard')

    reservations = Reservation.objects.filter(client=request.user).order_by('-date', '-heure')
    avis_prestataires_ids = Avis.objects.filter(client=request.user).values_list('prestataire_id', flat=True)
    return render(request, 'reservation/mes_reservations.html', {
        'reservations': reservations,
        'avis_prestataires_ids': avis_prestataires_ids,
    })

# ajouter un service


# profil complet de prestataire
@login_required
def completer_profil_prestataire(request):
    user = request.user

    if user.role != 'prestataire':
        messages.error(request, "Seuls les prestataires peuvent accéder à cette page.")
        return redirect('dashboard')

    try:
        Prestataire.objects.get(utilisateur=user)
        messages.info(request, "Votre profil prestataire existe déjà.")
        return redirect('dashboard')
    except Prestataire.DoesNotExist:
        pass

    if request.method == 'POST':
        form = PrestataireForm(request.POST, request.FILES)
        if form.is_valid():
            prestataire = form.save(commit=False)
            prestataire.utilisateur = user
            prestataire.save()
            messages.success(request, "Profil prestataire complété avec succès.")
            return redirect('dashboard')
    else:
        form = PrestataireForm()

    return render(request, 'reservation/completer_profil.html', {'form': form})


# avis
@login_required
def laisser_avis(request, prestataire_id):
    prestataire = get_object_or_404(Prestataire, id=prestataire_id)
    try:
        avis = Avis.objects.get(client=request.user, prestataire=prestataire)
        is_update = True
    except Avis.DoesNotExist:
        avis = None
        is_update = False

    if request.method == 'POST':
        form = AvisForm(request.POST, instance=avis)
        if form.is_valid():
            avis_obj = form.save(commit=False)
            avis_obj.client = request.user
            avis_obj.prestataire = prestataire
            avis_obj.save()
            return redirect('mes_reservations')
    else:
        form = AvisForm(instance=avis)

    return render(request, 'reservation/laisser_avis.html', {
        'form': form,
        'prestataire': prestataire,
        'is_update': is_update,
    })




def home_view(request):
    query = request.GET.get('q')

    # Annoter les services avec le nombre de prestataires (via ServiceOffert)
    services = Service.objects.annotate(
        nb_prestataires=Count('offres__prestataire', distinct=True)
    ).filter(nb_prestataires__gt=0)  # Afficher uniquement les services ayant au moins un prestataire

    if query:
        services = services.filter(
            Q(nom__icontains=query)
        )

    prestataires = Prestataire.objects.all()
    avis = Avis.objects.all()

    return render(request, 'reservation/home.html', {
        'services': services,
        'prestataires': prestataires,
        'avis': avis
    })


# mes services views
@login_required
def mes_services(request):
    if request.user.role != 'prestataire':
        return redirect('dashboard')

    try:
        prestataire = Prestataire.objects.get(utilisateur=request.user)
        services_offerts = ServiceOffert.objects.filter(prestataire=prestataire)
    except Prestataire.DoesNotExist:
        services_offerts = []

    return render(request, 'reservation/mes_services.html', {
        'services': services_offerts  # ✅ correction ici
    })



@login_required
def modifier_service(request, service_id):
    if request.user.role != 'prestataire':
        return redirect('dashboard')

    # On récupère l'objet ServiceOffert, pas Service !
    service_offert = get_object_or_404(ServiceOffert, pk=service_id, prestataire__utilisateur=request.user)

    if request.method == 'POST':
        form = ServiceOffertForm(request.POST, instance=service_offert)
        if form.is_valid():
            form.save()
            messages.success(request, "Le service a été mis à jour avec succès.")
            return redirect('mes_services')
    else:
        form = ServiceOffertForm(instance=service_offert)

    return render(request, 'reservation/modifier_service.html', {'form': form, 'service': service_offert})



@login_required
@require_POST
def supprimer_service(request, service_id):
    if request.user.role != 'prestataire':
        return redirect('dashboard')

    # On récupère l'objet ServiceOffert, pas Service !
    service_offert = get_object_or_404(ServiceOffert, pk=service_id, prestataire__utilisateur=request.user)

    service_offert.delete()
    messages.success(request, "Service supprimé avec succès.")
    return redirect('mes_services')

# service détails
def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    # On récupère tous les ServiceOffert pour ce service
    services_offerts = ServiceOffert.objects.filter(service=service)
    # On récupère les prestataires à partir des services offerts
    prestataires = [so.prestataire for so in services_offerts]

    return render(request, 'reservation/service_detail.html', {
        'service': service,
        'prestataires': prestataires,
        'services_offerts': services_offerts,  # Utile si tu veux afficher prix/description
    })

@login_required
def mes_reservations_prestataire(request):
    if request.user.role != 'prestataire':
        return redirect('dashboard')

    try:
        prestataire = Prestataire.objects.get(utilisateur=request.user)
        reservations = Reservation.objects.filter(service_offert__prestataire=prestataire).order_by('-date', '-heure')
    except Prestataire.DoesNotExist:
        reservations = []

    # Exemple dans views.py pour chaque réservation
    for r in reservations:
        r.nb_messages_non_lus = Message.objects.filter(
            reservation=r,
            recipient=request.user,
            is_read=False
        ).count()

    return render(request, 'reservation/mes_reservations_prestataire.html', {
    'reservations': reservations
    })

@login_required
@require_POST
def action_reservation(request, reservation_id, action):
    try:
        reservation = Reservation.objects.get(
            id=reservation_id,
            service_offert__prestataire__utilisateur=request.user
        )

        if reservation.statut != 'en_attente':
            messages.warning(request, "Cette réservation a déjà été traitée.")
        else:
            if action == 'accepter':
                reservation.statut = 'acceptée'
                notifier(
                    reservation.client,
                    f"Votre réservation pour {reservation.service_offert.service.nom} a été acceptée."
                )
            elif action == 'refuser':
                reservation.statut = 'refusée'
                notifier(
                    reservation.client,
                    f"Votre réservation pour {reservation.service_offert.service.nom} a été refusée."
                )
            elif action == 'reporter':
                # ... logique de report ...
                notifier(
                    reservation.client,
                    f"Le prestataire souhaite reporter votre réservation pour {reservation.service_offert.service.nom}."
                )
            reservation.save()
    except Reservation.DoesNotExist:
        messages.error(request, "Réservation introuvable ou accès non autorisé.")

    return redirect('mes_reservations_prestataire')

@login_required
@require_POST
def changer_statut_reservation(request, reservation_id, statut):
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    # Vérifie que l'utilisateur est bien le prestataire concerné
    if request.user != reservation.service_offert.prestataire.utilisateur:
        messages.error(request, "Accès non autorisé.")
        return redirect('mes_reservations_prestataire')

    # Autoriser uniquement à passer au statut "terminée"
    if reservation.statut == 'acceptée' and statut == 'terminée':
        reservation.statut = statut
        reservation.save()
        messages.success(request, "Réservation marquée comme terminée.")
    else:
        messages.warning(request, "Impossible de modifier le statut dans cet état.")

    return redirect('mes_reservations_prestataire')

@login_required
@require_POST
def action_reservation_client(request, reservation_id, action):
    try:
        reservation = Reservation.objects.get(
            id=reservation_id,
            client=request.user
        )
        if reservation.statut not in ['en_attente', 'acceptée']:
            messages.warning(request, "Vous ne pouvez pas modifier cette réservation.")
        else:
            if action == 'annuler':
                reservation.statut = 'annulée'
                notifier(
                    reservation.service_offert.prestataire.utilisateur,
                    f"Le client a annulé la réservation pour {reservation.service_offert.service.nom}."
                )
            elif action == 'reporter':
                # ... logique de report ...
                notifier(
                    reservation.service_offert.prestataire.utilisateur,
                    f"Le client souhaite reporter la réservation pour {reservation.service_offert.service.nom}."
                )
            reservation.save()
    except Reservation.DoesNotExist:
        messages.error(request, "Réservation introuvable ou accès non autorisé.")

    return redirect('mes_reservations')



@login_required
def reporter_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    # Vérifie que l'utilisateur est bien concerné
    is_client = (request.user == reservation.client)
    is_prestataire = (hasattr(request.user, 'prestataire') and reservation.service_offert.prestataire.utilisateur == request.user)
    if not (is_client or is_prestataire):
        messages.error(request, "Action non autorisée.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = ReporterReservationForm(request.POST)
        if form.is_valid():
            reservation.nouvelle_date = form.cleaned_data['nouvelle_date']
            reservation.nouvelle_heure = form.cleaned_data['nouvelle_heure']
            reservation.statut = 'en_attente_confirmation'
            reservation.reporteur = request.user
            reservation.save()
            messages.success(request, "Proposition de nouvelle date envoyée.")
            # Redirige vers la bonne page
            if is_client:
                return redirect('mes_reservations')
            else:
                return redirect('mes_reservations_prestataire')
    else:
        form = ReporterReservationForm()

    return render(request, 'reservation/reporter_reservation.html', {
        'form': form,
        'reservation': reservation
    })

@login_required
def confirmer_report(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    # Seule l'autre partie peut confirmer
    if request.user == reservation.client:
        is_other = reservation.service_offert.prestataire.utilisateur != request.user
    else:
        is_other = reservation.client != request.user
    if not is_other or reservation.statut != 'en_attente_confirmation':
        messages.error(request, "Action non autorisée ou réservation non en attente de confirmation.")
        return redirect('dashboard')

    if request.method == 'POST':
        # On confirme la nouvelle date
        reservation.date = reservation.nouvelle_date
        reservation.heure = reservation.nouvelle_heure
        reservation.nouvelle_date = None
        reservation.nouvelle_heure = None
        reservation.statut = 'reportée'
        reservation.reporteur = None
        reservation.save()
        messages.success(request, "Nouvelle date confirmée.")
        if request.user == reservation.client:
            # Le client confirme, notification au prestataire
            notifier(
                reservation.service_offert.prestataire.utilisateur,
                f"Le client a confirmé la nouvelle date pour la réservation du service {reservation.service_offert.service.nom}."
            )
            return redirect('mes_reservations')
        else:
            # Le prestataire confirme, notification au client
            notifier(
                reservation.client,
                f"Le prestataire a confirmé la nouvelle date pour votre réservation du service {reservation.service_offert.service.nom}."
            )
            return redirect('mes_reservations_prestataire')

    return render(request, 'reservation/confirmer_report.html', {
        'reservation': reservation
    })

@login_required
def detail_prestataire(request, prestataire_id):
    prestataire = get_object_or_404(Prestataire, id=prestataire_id)
    services_offerts = ServiceOffert.objects.filter(prestataire=prestataire)
    note_moyenne = Avis.objects.filter(prestataire=prestataire).aggregate(Avg('note'))['note__avg']
    reservations_terminees = False
    if request.user.is_authenticated and hasattr(request.user, 'role') and request.user.role == 'client':
        reservations_terminees = Reservation.objects.filter(
            client=request.user,
            service_offert__prestataire=prestataire,
            statut='terminée'
        ).exists()
    return render(request, 'reservation/detail_prestataire.html', {
        'prestataire': prestataire,
        'services_offerts': services_offerts,
        'note_moyenne': note_moyenne,
        'reservations_terminees': reservations_terminees,
    })

def communaute(request):
    # Annoter chaque prestataire avec sa note moyenne et le nombre d'avis
    prestataires = Prestataire.objects.annotate(
        note_moyenne=Avg('avis__note'),
        nb_avis=Count('avis')
    ).order_by('-note_moyenne', '-nb_avis')[:6]

    # Pour chaque prestataire, récupérer un avis (le plus récent par exemple)
    avis_par_prestataire = {}
    for p in prestataires:
        avis = p.avis_set.order_by('-date').first()
        avis_par_prestataire[p.id] = avis

    return render(request, 'reservation/communaute.html', {
        'prestataires': prestataires,
        'avis_par_prestataire': avis_par_prestataire,
    })


def page_prestataire(request):
    # Récupère les 6 meilleurs prestataires selon la note moyenne
    meilleurs_prestataires = Prestataire.objects.annotate(
        note_moyenne=Avg('avis__note'),
        nb_avis=Count('avis')
    ).order_by('-note_moyenne', '-nb_avis')[:6]

    return render(request, 'reservation/page_prestataire.html', {
        'meilleurs_prestataires': meilleurs_prestataires,
    })

from django.db.models import Count, Q

def page_services(request):
    query = request.GET.get('q', '')
    services = Service.objects.annotate(
        nb_offres=Count('offres')
    )
    if query:
        services = services.filter(nom__icontains=query)
    services = services.order_by('-nb_offres', 'nom')[:6]

    # Pour la datalist
    all_service_names = Service.objects.values_list('nom', flat=True).distinct()

    return render(request, 'reservation/page_services.html', {
        'services': services,
        'query': query,
        'all_service_names': all_service_names,
    })

def page_temoignages(request):
    query = request.GET.get('q', '')
    avis = Avis.objects.select_related('prestataire__utilisateur', 'client')
    if query:
        avis = avis.filter(prestataire__utilisateur__name__icontains=query)
    avis = avis.order_by('-note', '-date')[:6]

    return render(request, 'reservation/page_temoignages.html', {
        'avis': avis,
        'query': query,
    })



@login_required
def marquer_notification_lue(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, utilisateur=request.user)
    notification.lu = True
    notification.save()
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))

@login_required
def marquer_tout_lu(request):
    Notification.objects.filter(utilisateur=request.user, lu=False).update(lu=True)
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))

@login_required
def historique_notifications(request):
    notifications = Notification.objects.filter(utilisateur=request.user).order_by('-date')
    return render(request, 'reservation/historique_notifications.html', {'notifications': notifications})

@login_required
def supprimer_notification(request, notification_id):
    notif = get_object_or_404(Notification, id=notification_id, utilisateur=request.user)
    notif.delete()
    return redirect('historique_notifications')

@login_required
def supprimer_toutes_notifications(request):
    Notification.objects.filter(utilisateur=request.user).delete()
    return redirect('historique_notifications')

@login_required
def ajouter_service_offert(request):
    if request.method == 'POST':
        form = ServiceDatalistForm(request.POST)
        if form.is_valid():
            service_offert = form.save(commit=False)
            service_offert.prestataire = request.user.prestataire
            service_offert.save()
            messages.success(request, "Service ajouté avec succès!")
            return redirect('mes_services')
    else:
        form = ServiceDatalistForm()
    
    return render(request, 'reservation/ajouter_service.html', {
        'form': form,
        'services_autorises': SERVICES_AUTORISES
    })



@login_required
def boite_reception(request):
    messages_recus = Message.objects.filter(recipient=request.user).order_by('-created_at')
    nb_non_lus = Message.objects.filter(recipient=request.user, is_read=False).count()
    return render(request, 'reservation/boite_reception.html', {
        'messages_recus': messages_recus,
        'nb_non_lus': nb_non_lus,
    })

@login_required
def envoyer_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('boite_reception')
    else:
        form = MessageForm()
    return render(request, 'reservation/envoyer_message.html', {'form': form})


@login_required
def messages_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    messages_list = Message.objects.filter(reservation=reservation).order_by('created_at')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.reservation = reservation
            # Définir automatiquement le destinataire
            if request.user == reservation.client:
                message.recipient = reservation.service_offert.prestataire.utilisateur
            else:
                message.recipient = reservation.client
            message.save()
            # Créer une notification pour le destinataire
            Notification.objects.create(
                utilisateur=message.recipient,
                message=f"Nouveau message de {message.sender.name} concernant la réservation.",
                auto=True
            )
            return redirect('messages_reservation', reservation_id=reservation.id)
    else:
        form = MessageForm(initial={'reservation': reservation})
    # Marquer les messages comme lus pour l'utilisateur connecté
    Message.objects.filter(
        reservation=reservation,
        recipient=request.user,
        is_read=False
    ).update(is_read=True)
    return render(request, 'reservation/messages_reservation.html', {
        'reservation': reservation,
        'messages_list': messages_list,
        'form': form,
        'user': request.user,  # pour le template
    })

@login_required
def supprimer_message(request, message_id):
    msg = get_object_or_404(Message, id=message_id, sender=request.user)
    msg.delete()
    messages.success(request, "Message supprimé.")
    return redirect(request.META.get('HTTP_REFERER', 'boite_reception'))

@login_required
def refuser_report(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    # Remettre le statut précédent (ex : 'acceptée')
    if reservation.statut == 'en_attente_confirmation':
        reservation.nouvelle_date = None
        reservation.nouvelle_heure = None
        # Option : tu peux garder le statut précédent en mémoire si besoin
        reservation.statut = 'acceptée'
        reservation.save()
        messages.success(request, "Vous avez refusé le report de la réservation.")
    return redirect('mes_reservations' if request.user == reservation.client else 'mes_reservations_prestataire')

from django.contrib.auth import get_user_model

@login_required
def modifier_profil(request):
    user = request.user
    if hasattr(user, 'prestataire'):
        profil = user.prestataire
        FormClass = PrestataireForm
    else:
        profil = user
        FormClass = UserForm

    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil modifié avec succès.")
            return redirect('dashboard')
    else:
        form = FormClass(instance=profil)
    return render(request, 'reservation/modifier_profil.html', {'form': form})

@login_required
def supprimer_profil(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, "Votre profil a été supprimé.")
        return redirect('home')
    return render(request, 'reservation/supprimer_profil.html')

@login_required
def signaler_prestataire(request, prestataire_id):
    prestataire = get_object_or_404(Prestataire, id=prestataire_id)
    # Vérifier que l'utilisateur est client et a déjà réservé chez ce prestataire
    if not Reservation.objects.filter(client=request.user, service_offert__prestataire=prestataire, statut='terminée').exists():
        messages.error(request, "Vous ne pouvez signaler ce prestataire que si vous avez déjà réservé chez lui.")
        return redirect('mes_reservations')
    if request.method == 'POST':
        form = SignalementForm(request.POST, request.FILES)
        if form.is_valid():
            signalement = form.save(commit=False)
            signalement.prestataire = prestataire
            signalement.client = request.user
            signalement.save()
            # Notifier l'admin et le prestataire
            Notification.objects.create(
                utilisateur=prestataire.utilisateur,
                message=f"Vous avez été signalé pour {signalement.motif}. Vous pouvez vous défendre.",
                auto=True
            )
            # Envoi d'un email au prestataire
            send_mail(
                'Vous avez été signalé sur Elfeservice',
                f'Bonjour, vous avez été signalé pour le motif : {signalement.motif}.\n\nDescription : {signalement.description}\n\nConnectez-vous pour vous défendre.',
                'admin@elfeservice.com',
                [prestataire.utilisateur.email],
            )
            return redirect('mes_reservations')
    else:
        form = SignalementForm()
    return render(request, 'reservation/signaler_prestataire.html', {'form': form, 'prestataire': prestataire})

@login_required
def defense_signalement(request, signalement_id):
    signalement = get_object_or_404(Signalement, id=signalement_id, prestataire__utilisateur=request.user)
    if request.method == 'POST':
        defense = request.POST.get('defense')
        preuve = request.FILES.get('preuve_defense')
        signalement.defense = defense
        if preuve:
            signalement.preuve_defense = preuve
        signalement.save()
        messages.success(request, "Votre défense a été envoyée à l'administrateur.")
        return redirect('dashboard')
    return render(request, 'reservation/defense_signalement.html', {'signalement': signalement})

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Avg, Count

@staff_member_required
def dashboard_admin(request):
    # Top 6 prestataires les mieux notés
    top_prestataires = Prestataire.objects.annotate(
        moyenne=Avg('avis__note')
    ).order_by('-moyenne')[:6]

    # Tous les signalements
    signalements = Signalement.objects.select_related('prestataire', 'client').all().order_by('-date_signalement')

    return render(request, 'reservation/dashboard_admin.html', {
        'top_prestataires': top_prestataires,
        'signalements': signalements,
    })

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def avertir_prestataire(request, signalement_id):
    signalement = get_object_or_404(Signalement, id=signalement_id)
    if signalement.statut == 'en_attente':
        signalement.statut = 'averti'
        signalement.traite = True
        signalement.save()
        # Notifier le prestataire
        Notification.objects.create(
            utilisateur=signalement.prestataire.utilisateur,
            message=f"Vous avez été averti suite à un signalement pour : {signalement.motif}.",
            auto=True
        )
        # Envoi d'un email au prestataire
        send_mail(
            'Avertissement suite à un signalement',
            f'Bonjour, vous avez reçu un avertissement pour : {signalement.motif}.',
            'admin@elfeservice.com',
            [signalement.prestataire.utilisateur.email],
        )
        messages.success(request, "Prestataire averti.")
    return redirect('dashboard_admin')

@staff_member_required
def bannir_prestataire(request, signalement_id):
    signalement = get_object_or_404(Signalement, id=signalement_id)
    prestataire = signalement.prestataire
    user = prestataire.utilisateur

    # Sauvegarder les contacts dans une table "bannis"
    PrestataireBanni.objects.create(
        email=user.email,
        telephone=prestataire.telephone,
        nom=user.name
    )

    # Bannir le prestataire
    signalement.statut = 'banni'
    signalement.traite = True
    signalement.save()
    # Notifier le prestataire
    Notification.objects.create(
        utilisateur=user,
        message=f"Votre compte a été banni suite à un signalement pour : {signalement.motif}.",
        auto=True
    )
    # Envoi d'un email au prestataire
    send_mail(
        'Votre compte a été banni',
        f'Bonjour, votre compte a été banni suite à un signalement pour : {signalement.motif}.',
        'admin@elfeservice.com',
        [user.email],
    )
    # Supprimer le compte utilisateur et le profil prestataire
    prestataire.delete()
    user.delete()
    messages.success(request, "Prestataire banni et supprimé.")
    return redirect('dashboard_admin')

    # Vérifier si le prestataire est averti et a été signalé par au moins 2 clients différents
    signalements_avertis = Signalement.objects.filter(
        prestataire=prestataire,
        statut='averti'
    ).values('client').distinct().count()

    if prestataire.signalements.filter(statut='averti').exists() and signalements_avertis >= 2:
        # Bannir automatiquement
        user = prestataire.utilisateur
        PrestataireBanni.objects.create(
            email=user.email,
            telephone=prestataire.telephone,
            nom=user.name
        )
        # Mettre à jour tous les signalements en "banni"
        Signalement.objects.filter(prestataire=prestataire).update(statut='banni', traite=True)
        # Notifier le prestataire
        Notification.objects.create(
            utilisateur=user,
            message="Votre compte a été banni automatiquement suite à plusieurs signalements.",
            auto=True
        )
        # Supprimer le compte utilisateur et le profil prestataire
        prestataire.delete()
        user.delete()

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q

@staff_member_required
def messages_admin_prestataire(request, prestataire_id):
    prestataire = get_object_or_404(Prestataire, id=prestataire_id)
    admin_user = request.user
    # Récupérer tous les messages entre l'admin et ce prestataire
    messages_list = Message.objects.filter(
        Q(sender=admin_user, recipient=prestataire.utilisateur) |
        Q(sender=prestataire.utilisateur, recipient=admin_user)
    ).order_by('created_at')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = admin_user
            msg.recipient = prestataire.utilisateur
            msg.save()
            # (Optionnel) Notifier le prestataire par email
            send_mail(
                "Nouveau message de l'administrateur",
                "Vous avez reçu un nouveau message de l'administrateur sur Elfeservice.",
                'admin@elfeservice.com',
                [prestataire.utilisateur.email],
            )
            return redirect('messages_admin_prestataire', prestataire_id=prestataire.id)
    else:
        form = MessageForm()
    return render(request, 'reservation/messages_admin_prestataire.html', {
        'prestataire': prestataire,
        'messages_list': messages_list,
        'form': form,
        'user': request.user,
    })

from .models import NewsletterEmail

def newsletter_subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            if not NewsletterEmail.objects.filter(email=email).exists():
                NewsletterEmail.objects.create(email=email)
                messages.success(request, "Votre inscription à la newsletter a bien été prise en compte. Merci !")
            else:
                messages.info(request, "Cet email est déjà inscrit à la newsletter.")
        else:
            messages.error(request, "Veuillez entrer une adresse email valide.")
        return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def mes_signalements(request):
    signalements = Signalement.objects.filter(client=request.user)
    return render(request, 'reservation/mes_signalements.html', {
        'signalements': signalements
    })