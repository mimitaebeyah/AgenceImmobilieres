from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import  views as auth_views
from app.forms import LoginForm, MypasswordChangeForm, MyPasswordResetForm


urlpatterns = [
    path('', views.MaisonView.as_view(), name='maison'),

    path('maison-detail/<int:pk>', views.MaisonDetailView.as_view(), name='maison-detail'),

    path('contact/', views.Contact_Us, name='contact'),

    path('about/', views.About_us, name='about'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name = 'logout'),


    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',
    authentication_form=LoginForm), name='login'),


    path('profile', views.profile, name='profile'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MypasswordChangeForm), name='changepassword'),

    path('inscription/', views.EnregistrementClientView.as_view(), name ="EnregistrementClient"),
    
    path('ajouter_maison/', views.Ajoutermaison, name = "ajouter_maison"),

    path('Liste_maisons/', views.Liste_maisons, name ="Liste_maisons"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   