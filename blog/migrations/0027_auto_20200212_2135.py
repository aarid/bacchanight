# Generated by Django 2.2.9 on 2020-02-12 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_image_lien_musba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='lien_musba',
            field=models.CharField(max_length=200),
        ),
    ]
