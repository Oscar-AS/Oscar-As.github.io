from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import include, path
from cours.views import  manage_requests,accept_request, reject_request,Membre_publicateur, index,contact,connexion, register,home,index_evenement,index_cours,index_sujet,index_sujet_pres,index_sujet_sel,index_information,index_information_fil,index_information_site,formulaire_message, DemandePublicateurView, DemandeEnvoyeeView, ZoneAdminView, ApprouverDemandeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("cours.urls")),

    ##### CONNEXION  ###############

    path('login', connexion, name="connexion"),
    path('register', register, name="register"),

    path("Accueil/",index, name="index"),
    path("cours/",index_cours, name="index_cours"),
    


    path('contact/', contact, name='contact'),

    path("evenement/",index_evenement, name="index_evenement"),
    
    #path("cours/<str:fichier>",telechargé, name="telechargé"),
    path("sujet/",index_sujet, name="index_sujet"),
    path("sujet/selection/",index_sujet_sel, name="index_sujet_sel"),
    
    path("sujet/preselection/",index_sujet_pres, name="index_sujet_pres"),
    path("information/",index_information, name="index_information"),
    path("information/filière",index_information_fil, name="index_information_fil"),
    path("information/site",index_information_site, name="index_information_site"),
    path('message/',formulaire_message, name='formulaire_message'),


## Chemin pour la création d'un compte utilisateur




    path('membership_request/', Membre_publicateur, name='Membre_publicateur'),
    path('manage_requests/', manage_requests, name='manage_requests'),
    path('accept_request/<int:request_id>/', accept_request, name='accept_request'),
    path('reject_request/<int:request_id>/', reject_request, name='reject_request'),



    path('demande-publicateur/', DemandePublicateurView.as_view(), name='demande_publicateur'),
    path('demande-envoyee/', DemandeEnvoyeeView.as_view(), name='demande_envoyee'),
    path('zone-admin/', ZoneAdminView.as_view(), name='zone_admin'),
    path('approuver-demande/<int:pk>/', ApprouverDemandeView.as_view(), name='approuver_demande'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)