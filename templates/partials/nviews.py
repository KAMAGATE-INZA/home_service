from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Avg, Q
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.apps import apps

from .models import (
    Service, Prestataire, Reservation, Avis, ServiceOffert, 
    Message, Signalement, PrestataireBanni, NewsletterEmail
)
from .forms import (
    ReservationForm, ServiceForm, AvisForm, ServiceOffertForm,
    MessageForm, SignalementForm, ServiceDatalistForm, 
    PrestataireForm, UserForm, AjouterServiceExistForm,
    NouveauServiceForm, ReporterReservationForm
)
from .utils import notifier, SERVICES_AUTORISES

Notification = apps.get_model('reservation', 'Notification')  # ✅

# ====== HOME & SEARCH ======
def home_view(request):
    query = request.GET.get('q')
    services = Service.objects.annotate(nb_prestataires=Count('offres')).filter(nb_prestataires__gt=0)
    if query:
        services = services.filter(nom__icontains=query)
    prestataires = Prestataire.objects.all()
    avis = Avis.objects.all()
    return render(request, 'reservation/home.html', {
        'services': services,
        'prestataires': prestataires,
        'avis': avis
    })

def page_services(request):
    query = request.GET.get('q', '')
    services = Service.objects.annotate(nb_offres=Count('offres'))
    if query:
        services = services.filter(nom__icontains=query)
    services = services.order_by('-nb_offres', 'nom')[:6]
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

# ====== RÉSERVATION ======
@login_required
def reserver_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.user.role != 'client':
        messages.error(request, "Seuls les clients peuvent réserver un service.")
        return redirect('dashboard')
    prestataire_id = request.GET.get('prestataire')
    prestataire = get_object_or_404(Prestataire, pk=prestataire_id)
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
            conflit = Reservation.objects.filter(
                service_offert=service_offert,
                date=date,
                heure=heure,
                statut__in=['en_attente', 'acceptée']
            ).exists()
            if conflit:
                messages.error(request, "Ce créneau est déjà réservé.")
            else:
                reservation = form.save(commit=False)
                reservation.client = request.user
                reservation.service_offert = service_offert
                reservation.save()
                notifier(prestataire.utilisateur, f"Nouvelle réservation pour {service.nom}")
                messages.success(request, "Réservation effectuée.")
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

# ====== MES SERVICES ======
@login_required
def mes_services(request):
    if request.user.role != 'prestataire':
        return redirect('dashboard')
    try:
        prestataire = Prestataire.objects.get(utilisateur=request.user)
        services_offerts = ServiceOffert.objects.filter(prestataire=prestataire).select_related('service')
    except Prestataire.DoesNotExist:
        services_offerts = []
    return render(request, 'reservation/mes_services.html', {
        'services': services_offerts
    })

@login_required
def ajouter_service_offert(request):
    if request.method == 'POST':
        form = ServiceDatalistForm(request.POST)
        if form.is_valid():
            service_offert = form.save(commit=False)
            service_offert.prestataire = request.user.prestataire
            service_offert.save()
            messages.success(request, "Service ajouté avec succès !")
            return redirect('mes_services')
    else:
        form = ServiceDatalistForm()
    return render(request, 'reservation/ajouter_service.html', {
        'form': form,
        'services_autorises': SERVICES_AUTORISES
    })

@login_required
def modifier_service(request, service_id):
    service_offert = get_object_or_404(ServiceOffert, pk=service_id, prestataire__utilisateur=request.user)
    if request.method == 'POST':
        form = ServiceOffertForm(request.POST, instance=service_offert)
        if form.is_valid():
            form.save()
            messages.success(request, "Le service a été mis à jour avec succès.")
            return redirect('mes_services')
    else:
        form = ServiceOffertForm(instance=service_offert)
    return render(request, 'reservation/modifier_service.html', {
        'form': form,
        'service': service_offert
    })

@login_required
@require_POST
def supprimer_service(request, service_id):
    service_offert = get_object_or_404(ServiceOffert, pk=service_id, prestataire__utilisateur=request.user)
    service_offert.delete()
    messages.success(request, "Service supprimé avec succès.")
    return redirect('mes_services')

# ====== AVIS ======
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
            messages.success(request, "Avis enregistré.")
            return redirect('mes_reservations')
    else:
        form = AvisForm(instance=avis)

    return render(request, 'reservation/laisser_avis.html', {
        'form': form,
        'prestataire': prestataire,
        'is_update': is_update,
    })

# ====== PROFIL PRESTATAIRE ======
@login_required
def completer_profil_prestataire(request):
    user = request.user
    if user.role != 'prestataire':
        messages.error(request, "Seuls les prestataires peuvent accéder à cette page.")
        return redirect('dashboard')
    if Prestataire.objects.filter(utilisateur=user).exists():
        messages.info(request, "Votre profil prestataire existe déjà.")
        return redirect('dashboard')

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

@login_required
def mes_reservations_prestataire(request):
    if request.user.role != 'prestataire':
        return redirect('dashboard')

    try:
        prestataire = Prestataire.objects.get(utilisateur=request.user)
        reservations = Reservation.objects.filter(service_offert__prestataire=prestataire).order_by('-date', '-heure')
    except Prestataire.DoesNotExist:
        reservations = []

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
def messages_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    messages_list = Message.objects.filter(reservation=reservation).order_by('created_at')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.reservation = reservation
            message.recipient = reservation.client if request.user == reservation.service_offert.prestataire.utilisateur else reservation.service_offert.prestataire.utilisateur
            message.save()

            # Notification automatique
            Notification = apps.get_model('reservation', 'Notification')
            Notification.objects.create(
                utilisateur=message.recipient,
                message=f"Nouveau message concernant la réservation du {reservation.date}",
                auto=True
            )
            return redirect('messages_reservation', reservation_id=reservation.id)
    else:
        form = MessageForm()

    Message.objects.filter(
        reservation=reservation,
        recipient=request.user,
        is_read=False
    ).update(is_read=True)

    return render(request, 'reservation/messages_reservation.html', {
        'reservation': reservation,
        'messages_list': messages_list,
        'form': form
    })

@login_required
def marquer_notification_lue(request, notification_id):
    Notification = apps.get_model('reservation', 'Notification')
    notif = get_object_or_404(Notification, id=notification_id, utilisateur=request.user)
    notif.lu = True
    notif.save()
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))

@login_required
def marquer_tout_lu(request):
    Notification = apps.get_model('reservation', 'Notification')
    Notification.objects.filter(utilisateur=request.user, lu=False).update(lu=True)
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))

@login_required
def historique_notifications(request):
    Notification = apps.get_model('reservation', 'Notification')
    notifications = Notification.objects.filter(utilisateur=request.user).order_by('-date')
    return render(request, 'reservation/historique_notifications.html', {'notifications': notifications})

@login_required
def supprimer_notification(request, notification_id):
    Notification = apps.get_model('reservation', 'Notification')
    notif = get_object_or_404(Notification, id=notification_id, utilisateur=request.user)
    notif.delete()
    return redirect('historique_notifications')

@login_required
def supprimer_toutes_notifications(request):
    Notification = apps.get_model('reservation', 'Notification')
    Notification.objects.filter(utilisateur=request.user).delete()
    return redirect('historique_notifications')

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

@staff_member_required
def dashboard_admin(request):
    top_prestataires = Prestataire.objects.annotate(
        moyenne=Avg('avis__note')
    ).order_by('-moyenne')[:6]

    signalements = Signalement.objects.select_related('prestataire', 'client').all().order_by('-date_signalement')

    return render(request, 'reservation/dashboard_admin.html', {
        'top_prestataires': top_prestataires,
        'signalements': signalements,
    })

@staff_member_required
def avertir_prestataire(request, signalement_id):
    signalement = get_object_or_404(Signalement, id=signalement_id)
    if signalement.statut == 'en_attente':
        signalement.statut = 'averti'
        signalement.traite = True
        signalement.save()

        Notification = apps.get_model('reservation', 'Notification')
        Notification.objects.create(
            utilisateur=signalement.prestataire.utilisateur,
            message=f"Vous avez été averti suite à un signalement : {signalement.motif}.",
            auto=True
        )

        send_mail(
            'Avertissement suite à un signalement',
            f"Bonjour, vous avez reçu un avertissement : {signalement.motif}.",
            'admin@elfeservice.com',
            [signalement.prestataire.utilisateur.email],
        )
        messages.success(request, "Prestataire averti.")
    return redirect('dashboard_admin')

@staff_member_required
def bannir_prestataire(request, signalement_id):
    signalement = get_object_or_404(Signalement, id=signalement_id)
    prestataire = signalement.prestataire
    utilisateur = prestataire.utilisateur

    PrestataireBanni.objects.create(
        email=utilisateur.email,
        telephone=getattr(prestataire, 'telephone', 'Inconnu'),
        nom=utilisateur.name
    )

    signalement.statut = 'banni'
    signalement.traite = True
    signalement.save()

    Notification = apps.get_model('reservation', 'Notification')
    Notification.objects.create(
        utilisateur=utilisateur,
        message=f"Votre compte a été banni suite à un signalement : {signalement.motif}.",
        auto=True
    )

    send_mail(
        'Compte banni',
        f'Votre compte a été banni suite au signalement : {signalement.motif}.',
        'admin@elfeservice.com',
        [utilisateur.email],
    )

    prestataire.delete()
    utilisateur.delete()
    messages.success(request, "Prestataire supprimé et banni.")
    return redirect('dashboard_admin')

@login_required
def supprimer_profil(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, "Votre profil a été supprimé.")
        return redirect('home')
    return render(request, 'reservation/supprimer_profil.html')

def newsletter_subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            if not NewsletterEmail.objects.filter(email=email).exists():
                NewsletterEmail.objects.create(email=email)
                messages.success(request, "Inscription à la newsletter réussie !")
            else:
                messages.info(request, "Cet email est déjà inscrit.")
        else:
            messages.error(request, "Adresse email invalide.")
        return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def boite_reception(request):
    messages_recus = Message.objects.filter(recipient=request.user).order_by('-created_at')
    nb_non_lus = Message.objects.filter(recipient=request.user, is_read=False).count()
    return render(request, 'reservation/boite_reception.html', {
        'messages_recus': messages_recus,
        'nb_non_lus': nb_non_lus
    })

@login_required
def supprimer_message(request, message_id):
    msg = get_object_or_404(Message, id=message_id, sender=request.user)
    msg.delete()
    messages.success(request, "Message supprimé.")
    return redirect(request.META.get('HTTP_REFERER', 'boite_reception'))
