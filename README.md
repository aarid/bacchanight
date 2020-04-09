# bacchanight

Pour lancer le serveur du site avec Django certaines configuration sont nécessaires:

- Créez un environnement virtuel *env* :
    python3 -m venv env

- Placer vous à l'intérieur et installer les applications de Django:
    source myvenv/bin/activate

    + Mettre à jour pip:
        python -m pip install --upgrade pip  
        pip install -r requirements.txt

    + La bibliothèque Pillow pour les images:
        pip install Pillow 

    + django-cleanup pour supprimer les fichiers des objets supprimés : 
        pip install django-cleanup


- Lancement du serveur:
    python manage.py runserver


- Migration des tables (pour actualiser les modifications faites dans le code) : 
    python manage.py makemigrations blog

- Application des migrations avec: 
    python manage.py migrate blog

