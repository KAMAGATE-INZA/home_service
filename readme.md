# 🧹 Elfeservice – Plateforme de Réservation de Services à Domicile

Ce projet Django permet aux **clients** de réserver des services (plomberie, coiffure, nettoyage, etc.) proposés par des **prestataires**. Il inclut :
- authentification,
- gestion des profils,
- réservation,
- avis,
- messagerie,
- signalement,
- tableau de bord admin,
- ajout dynamique de services avec MySQL.

---

## ⚙️ Prérequis

- Python 3.10 ou +
- MySQL Server (8.x recommandé)
- Git
- (optionnel) VS Code

---

## 🚀 Installation locale

```bash
# 1. Cloner le projet
git clone https://github.com/KAMAGATE-INZA/home_service.git
cd home_service

# 2. Créer un environnement virtuel
python -m venv venv
# Windows :
venv\Scripts\activate
# Linux/macOS :
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer la base de données
# Copiez le fichier .env.example en .env et remplissez les bonnes infos

# 5. Appliquer les migrations
python manage.py migrate

# 6. Créer un superutilisateur (compte admin)
python manage.py createsuperuser

# 7. Lancer le serveur
python manage.py runserver

# 📦 Base de données MySQL
DB_NAME=home_service
DB_USER=Kamagate Inza
DB_PASSWORD=@14285948S
DB_HOST=localhost
DB_PORT=3306