# Generated by Django 2.2.7 on 2020-02-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20200223_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='inclu',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
