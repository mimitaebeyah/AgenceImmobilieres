# Generated by Django 4.0 on 2022-01-29 13:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_maison_etat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commandes',
            old_name='date_commande',
            new_name='date_debut_location',
        ),
        migrations.AddField(
            model_name='commandes',
            name='date_fin_location',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
