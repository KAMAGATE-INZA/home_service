from django.apps import apps
Notification = apps.get_model('reservation', 'Notification')

def notifications_count(request):
    if request.user.is_authenticated:
        nb_notifications_non_lues = Notification.objects.filter(utilisateur=request.user, lu=False).count()
    else:
        nb_notifications_non_lues = 0
    return {'nb_notifications_non_lues': nb_notifications_non_lues}