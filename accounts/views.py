from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.apps import apps


from django.forms import inlineformset_factory
from accounts.models import ContactUtilisateur,CustomUser
from .forms import CustomUserCreationForm, CustomAuthenticationForm,ContactUtilisateurForm
from reservation.models import Reservation, Service, Prestataire, Avis


ContactFormSet = inlineformset_factory(
    CustomUser, ContactUtilisateur,
    form=ContactUtilisateurForm,  # ← ici
    extra=1,
    can_delete=True
)

# Vue d'inscription
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        contact_formset = ContactFormSet(request.POST)

        if form.is_valid() and contact_formset.is_valid():
            user = form.save()
            contact_formset.instance = user
            contact_formset.save()
            messages.success(request, "Inscription réussie. Vous pouvez maintenant vous connecter.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        contact_formset = ContactFormSet()

    return render(request, 'accounts/register.html', {
        'form': form,
        'contact_formset': contact_formset
    })

# ✅ Vue de connexion
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


# ✅ Déconnexion
def logout_view(request):
    logout(request)
    return redirect('login')


# ✅ Profil utilisateur connecté
@login_required
def profil_view(request):
    user = request.user
    context = {'user': user}

    if user.role == 'client':
        context['reservations'] = Reservation.objects.filter(client=user)

    elif user.role == 'prestataire':
        try:
            prestataire = Prestataire.objects.get(utilisateur=user)
            offres = prestataire.offres.select_related('service')  # ✅ correction ici
            demandes = Reservation.objects.filter(service_offert__prestataire=prestataire)
            context.update({
                'prestataire': prestataire,
                'offres': offres,
                'demandes': demandes
            })
        except Prestataire.DoesNotExist:
            context['prestataire'] = None

    return render(request, 'accounts/profil.html', context)


# ✅ Tableau de bord (client et prestataire)
@login_required
def dashboard_view(request):
    user = request.user
    Notification = apps.get_model('reservation', 'Notification')

    context = {
        'user': user,
        'has_prestataire_profile': False,
        'notifications': Notification.objects.filter(utilisateur=user, lu=False, auto=False).order_by('-date'),
        'notifications_auto': Notification.objects.filter(utilisateur=user, lu=False, auto=True).order_by('-date'),
    }

    if user.role == 'client':
        context.update({
            'reservations': Reservation.objects.filter(client=user),
            'dernier_avis': Avis.objects.filter(client=user).order_by('-id').first()
        })

    elif user.role == 'prestataire':
        try:
            prestataire = Prestataire.objects.get(utilisateur=user)
            services = prestataire.offres.select_related('service')
            demandes = Reservation.objects.filter(service_offert__prestataire=prestataire)
            note_moyenne = Avis.objects.filter(prestataire=prestataire).aggregate(Avg('note'))['note__avg'] or 0
            context.update({
                'has_prestataire_profile': True,
                'services': services,
                'demandes': demandes,
                'note_moyenne': round(note_moyenne, 1)
            })
        except Prestataire.DoesNotExist:
            pass

    return render(request, 'accounts/dashboard.html', context)


# ✅ Vue de statistiques graphiques (prestataire uniquement)
@login_required
def statistiques_view(request):
    if request.user.role != 'prestataire':
        return redirect('dashboard')

    prestataire = get_object_or_404(Prestataire, utilisateur=request.user)
    reservations = Reservation.objects.filter(service_offert__prestataire=prestataire)

    stats = reservations.values('statut').annotate(count=Count('id'))
    labels = [s['statut'] for s in stats]
    data = [s['count'] for s in stats]

    return render(request, 'accounts/statistiques.html', {
        'labels': labels,
        'data': data
    })

@login_required
def ajouter_contact(request):
    if request.method == 'POST':
        form = ContactUtilisateurForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.utilisateur = request.user
            contact.save()
            messages.success(request, "Contact ajouté avec succès.")
            return redirect('profil')  # Redirige vers la page du profil
    else:
        form = ContactUtilisateurForm()

    return render(request, 'accounts/ajouter_contact.html', {'form': form})
@login_required
def modifier_contact(request, contact_id):
    contact = get_object_or_404(ContactUtilisateur, id=contact_id, utilisateur=request.user)

    if request.method == 'POST':
        form = ContactUtilisateurForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact mis à jour avec succès.")
            return redirect('profil')
    else:
        form = ContactUtilisateurForm(instance=contact)

    return render(request, 'accounts/modifier_contact.html', {'form': form})

@login_required
def supprimer_contact(request, contact_id):
    contact = get_object_or_404(ContactUtilisateur, id=contact_id, utilisateur=request.user)

    if request.method == 'POST':
        contact.delete()
        messages.success(request, "Contact supprimé avec succès.")
        return redirect('profil')

    return render(request, 'accounts/supprimer_contact.html', {'contact': contact})