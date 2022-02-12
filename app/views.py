from multiprocessing import context
from urllib import request
from django.shortcuts import render , redirect
from django.views import View
from app.forms import EnregistrementClientForm
from .models import Client, Maison, Ventes, Commandes
from .forms import EnregistrementClientForm
from django.contrib import messages
from .forms import Isertmaison
from app import views
from app.filters import Maisonfilter


class MaisonView(View):
    def get(self, request):
        ARAFAT = Maison.objects.filter(commune='A')
        ELMINA = Maison.objects.filter(commune='EM')
        DARNAIIM = Maison.objects.filter(commune='DN')
        TEYARET = Maison.objects.filter(commune='T')
        TEVRAGHZEINA = Maison.objects.filter(commune='TZ')
        SEBKHA = Maison.objects.filter(commune='S')
        RIYAD = Maison.objects.filter(commune='R')
        return render(request, 'app/maison.html', {'ARAFAT':ARAFAT, 'ELMINA':ELMINA,'DARNAIIM':DARNAIIM, 'TEYARET':TEYARET, 'TEVRAGHZEINA':TEVRAGHZEINA, 'SEBKHA':SEBKHA, 'RIYAD':RIYAD})


# def MaisonAll(request):
#     if not request.user.is_authenticated:
#         return redirect("/connexion")
#     if request.method == "POST":
#         titre = request.POST['titre']
#         date_debut = request.POST['date_debut']
#         date_fin = request.POST['date_fin']
#         description = request.POST['description']
#         quartier = request.POST['quartier']
#         commune = request.POST['commune']
#         image_maison = request.POST['image_maison']
#         description = request.POST['description']
#         Etat = request.POST['Etat']
#         maison = Maison.objects.get(user=user)
#         creatmaison = Maison.objects.create(maison=maison, titre=titre,date_debut=date_debut, date_fin=date_fin, quartier=quartier, commune=commune, image_maison=image_maison, description=description, Etat=Etat)
#         creatmaison.save()
#         alert = True
#         return render(request, "ajoutmaison.html", {'alert':alert})
#     return render(request, "ajoutmaison.html")

# def liste_des_maison(request):
#     if not request.user.is_authenticated:
#         return redirect("/connexion")
#     maison = Maison.objects.get(user=request.user)
#     maisonall =MaisonAll.objects.all()
#     return render(request, "liste_des_maison.html", {'maisonall':maisonall})

class MaisonDetailView(View):
    def get(self, request, pk):
        maison = Maison.objects.get(pk=pk)
        return render(request, 'app/maisonDetail.html', {'maison':maison})


class EnregistrementClientView(View):
    def get(self, request):
        form = EnregistrementClientForm()
        return render(request, 'app/inscription.html', {'form':form})

    def post(self, request):
        form  = EnregistrementClientForm(request.POST) 
        if form.is_valid():
            messages.success(request, 'congratilations!! Registered Successfully')
            form.save()
        return render(request, 'app/inscription.html', {'form':form})   


def checkout(request):
  return render(request, 'app/checkout.html')
  
def Contact_Us(request):
 return render(request, 'app/contact.html')

def About_us(request):
 return render(request, 'app/about.html')


def profile(request):
 return render(request, 'app/profile.html')



# def address(request):
#  return render(request, 'app/address.html')

# def orders(request):
#  return render(request, 'app/orders.html')
 

# def change_password(request):
#  return render(request, 'app/changepassword.html')


def Ajoutermaison(request):
    form=Isertmaison()
    if request.method == 'POST':
        form=Isertmaison(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            Prix = request.POST.get('Prix')
            Prix_reduit = request.POST.get('Prix_reduit')
            description = request.POST.get('description')
            quartier = request.POST.get('quartier')
            commune = request.POST.get('commune')
            image_maison = request.POST.get('image_maison')
            Etat = request.POST.get('Etat')
            maison = Maison.objects.create(title=title, Prix=Prix, Prix_reduit=Prix_reduit, description=description,quartier=quartier, commune=commune, image_maison=image_maison,Etat=Etat)
            form.save()
            return redirect('ajouter_client')
    context={'form':form}
    return render(request, 'app/ajouter_maison.html', context)



# def AjouterMaison(request):
#     form=Isertmaison()
#     if request.method == "POST":
#         form=Isertmaison(request.POST)
#         if form.is_valid():
#             form.save() 
#             return redirect('/')
#     context={'form':form }
#     return render(request, 'app/ajouter_maison.html',context)
    
def Liste_maisons(request):
    
    maison = Maison.objects.all()
    myFilter=Maisonfilter(request.GET, queryset=maison)
    maison = myFilter.qs
    context={'maison':maison, 'myFilter':myFilter}
    return render(request, 'app/listeMaison.html', context)