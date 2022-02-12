from dataclasses import fields
import django_filters

from .models import *

class Maisonfilter(django_filters.FilterSet):

    
    class Meta:
        model = Maison
        fields = ['title','Prix','Prix_reduit','description', 'quartier', 'commune', 'image_maison','Etat']
        #filtrage uniquement par etat communne
        exclude =['title','Prix','Prix_reduit', 'description', 'image_maison']