# Generated by Django 2.2.7 on 2019-11-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='name2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]