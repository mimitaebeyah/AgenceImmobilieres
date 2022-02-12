from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator

STATE_CHOICES = (
    ('Noudhibou','trarza'),
    ('brakna', 'lhewd_chargui'), 
    ('brakna', 'lhewd_chargui'),
    ( 'l3saba', 'lhewd lguarbi'),
    ('l3saba', 'lhewd lguarbi'),
    ('l3saba', 'lhewd lguarbi'),
    ('adrar','inchiri'),
)

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)   
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=50)
    Num_tel = models.IntegerField()
    State = models.CharField(choices=STATE_CHOICES, max_length=50)


def __str__(self):
    return str(self.id)

CHOIX_COMMUNE = (
    ('A', 'ARAFAT'),
    ('EM', 'EL MINA'),
    ('DN', 'DAR NAIIM'),
    ('T', 'TEYARET'),
    ('TZ', 'TEVRAGH ZEINA'),
    ('TG', 'TOUJOUNUT'),
    ('S', 'SEBKHA'),
    ('R', 'RIYAD'),
)

STATUS_CHOICE = (
    ('Libre', 'libre'),
    ('Occupé', 'Occupé'),

)
class Maison(models.Model):
    title = models.CharField(max_length=100)
    Prix = models.FloatField()
    Prix_reduit = models.FloatField()
    #date_debut = models.DateField()
    #date_debut = models.DateField()
    description = models.TextField()
    quartier = models.CharField(max_length=100)
    commune = models.CharField( choices=CHOIX_COMMUNE ,max_length=2)
    image_maison = models.ImageField(upload_to='maisonimg')
    Etat = models.CharField(max_length=50, choices=STATUS_CHOICE, default='Libre')
def __str__(self):
    return str(self.id)

class Ventes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Maison = models.ForeignKey(Maison, on_delete=models.CASCADE)
    prix = models.PositiveIntegerField(default=0)

def __str__(self):
    return str(self.id)

STATUS_CHOICES = (
    ('Accepté', 'Accepté'),
    ('Annuler', 'Annuler'),
    ('en_attendant', 'en_attendant')
)

class Commandes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE)
    prix = models.PositiveIntegerField(default=0)
    date_commande = models.DateTimeField(auto_now_add=True)
    Statut = models.CharField(max_length=50, choices=STATUS_CHOICES, default='en_attendant')

    



