# bacchanight

J'ai fait ce fichier pour qu'on ne galère pas à chercher les commandes à chaque fois

Il faut tout d'abord créer son propre environnement virtuel (qui doit écraser myvenv):
    python3 -m venv myvenv

    source myvenv/bin/activate
    python -m pip install --upgrade pip  (ou python3 et pip3 aussi)
    pip install -r requirements.txt

Il faut aussi installer la bibliothèque Pillow avec :
    pip3 install Pillow (avec sudo pour ordi perso)

Mot de passe page admin : azerty1234
Mot de passe passe admin : azerty1234

Pour lancer le serveur :
    python manage.py runserver ou python3 manage.py runserver

Adresse des pages : 
    Page d'accueuil : http://127.0.0.1:8000
    
    Page d'admin : http://127.0.0.1:8000/admin/
    
    Pythonanywhere (attention n'est pas toujours actualisé avec git) : http://aaridouane.pythonanywhere.com/

Créer les tables (faire la migration) : 
    python manage.py makemigrations blog

    Appliquer ces migrations avec : python manage.py migrate blog


Liens utiles pour les sites : 
    Djangogirls : https://tutorial.djangogirls.org/fr/

    Openclassroom : https://openclassrooms.com/fr/courses/4425076-decouvrez-le-framework-django/4631346-ajoutez-des-relations-entre-les-modeles

    Queryset : https://python.doctor/page-django-query-set-queryset-manager

    Queryset: https://docs.djangoproject.com/fr/3.0/ref/models/querysets/

    Pour les Forms : https://docs.djangoproject.com/fr/2.1/topics/forms/
