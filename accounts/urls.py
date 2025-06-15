from django.urls import path
from . import views
from .views import register_view, login_view, logout_view, profil_view,dashboard_view,statistiques_view

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profil/', profil_view, name='profil'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/statistiques/', statistiques_view, name='statistiques'),

]
