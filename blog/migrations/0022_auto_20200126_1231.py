# Generated by Django 2.2.8 on 2020-01-26 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20200125_2002'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Avis',
        ),
        migrations.DeleteModel(
            name='Joueur',
        ),
    ]
