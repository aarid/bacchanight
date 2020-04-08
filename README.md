# bacchanight

J'ai fait ce fichier pour qu'on ne galère pas à chercher les commandes à chaque fois

Il faut tout d'abord créer son propre environnement virtuel (qui doit écraser myvenv):
    python3 -m venv myvenv

    source myvenv/bin/activate
    python -m pip install --upgrade pip  (ou python3 et pip3 aussi)
    pip install -r requirements.txt

Il faut aussi installer la bibliothèque Pillow avec :
    pip3 install Pillow (avec sudo pour ordi perso)

Et cleanup pour supprimer les fichiers des objets supprimés : 
    pip install django-cleanup

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

    Pour changer l'affichage de la page admin : 
        https://python.doctor/page-django-interface-admin-administration-settings-django-contrib-auth

        Et aussi : https://docs.djangoproject.com/fr/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display

    Pour l'affichage des images:
        https://openclassrooms.com/fr/courses/1871271-developpez-votre-site-web-avec-le-framework-django/1872634-la-gestion-des-fichiers

Liaisons des salles 

Salle 1(Abdoulaye & Mouctar) ---> Les années 1910-1940 : du cubisme au retour à l'ordre (clé = 10)

Salle 2(Saliou) ---> Odilon Redon et l'art autour de 1900 (clé = 13)

Salle 3(Ousmane) ---> Impressionnisme et naturalisme (clé = 9)

Salle 4(Ibrahim) ---> Paysages et peinture animalière (clé = 14)

Salle 5(Aguibou) ---> Le renouveau de la peinture d'histoire entre académisme et réalisme (clé = 11)

Salle 6(Ibrahim & Mouctar) ---> Les années romantiques et la peinture d'histoire (clé = 12)
