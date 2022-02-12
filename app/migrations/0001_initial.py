# Generated by Django 4.0 on 2022-01-11 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=50)),
                ('Num_tel', models.IntegerField()),
                ('State', models.CharField(choices=[('Noudhibou', 'trarza'), ('brakna', 'lhewd_chargui'), ('brakna', 'lhewd_chargui'), ('l3saba', 'lhewd lguarbi'), ('l3saba', 'lhewd lguarbi'), ('l3saba', 'lhewd lguarbi'), ('adrar', 'inchiri')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Maison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Prix_de_vente', models.FloatField()),
                ('Prix_reduit', models.FloatField()),
                ('description', models.TextField()),
                ('quartier', models.CharField(max_length=100)),
                ('commune', models.CharField(choices=[('A', 'ARAFAT'), ('EM', 'EL MINA'), ('DN', 'DAR NAIIM'), ('T', 'TEYARET'), ('TZ', 'TEVRAGH ZEINA'), ('TG', 'TOUJOUNUT'), ('S', 'SEBKHA'), ('R', 'RIYAD')], max_length=2)),
                ('image_maison', models.ImageField(upload_to='maisonimg')),
            ],
        ),
        migrations.CreateModel(
            name='Ventes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.PositiveIntegerField(default=0)),
                ('Maison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.maison')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Commandes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.PositiveIntegerField(default=0)),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
                ('Statut', models.CharField(choices=[('Accepté', 'Accepté'), ('Annuler', 'Annuler'), ('en_attendant', 'en_attendant')], default='en_attendant', max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
                ('maison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.maison')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
