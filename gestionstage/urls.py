"""gestionstage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from stage.views import Ajouter_Enseignant, recherche,index,Ajouter_stagiaire,index2,index3,index4,index5,index,Ajouter_Stage,Ajouter_Organisme,Ajouter_Membre,Ajouter_Jury,Ajouter_Convention,Ajouter_Fiche

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('Liste_Enseignant/', index),
    path('Liste_Enseignant/', recherche),
    path('Liste_Stagiaire/', index2),
    path('Liste_Stage/', index3),   
    path('Liste_Organismes/', index4),
    path('Liste_Membre/', index5),
    #path('Liste_Enseignant/', recherche ,name="Listing"),
    path('Ajouter_Enseignant/', Ajouter_Enseignant,name="Listing"),
    path('Ajouter_Stagiaire/', Ajouter_stagiaire,name="Listing"),
    path('Ajouter_Stage/', Ajouter_Stage,name="Listing"),
    path('Ajouter_Organisme/', Ajouter_Organisme,name="Listing"),
    path('Ajouter_Membre/', Ajouter_Membre,name="Listing"),
    path('Ajouter_Jury/', Ajouter_Jury,name="Listing"),
    path('Ajouter_Convention/', Ajouter_Convention,name="Listing"),
    path('Ajouter_Fiche/', Ajouter_Fiche,name="Listing"),
]






