from contextlib import redirect_stderr
from multiprocessing import context
from django.shortcuts import render
from .forms import EnseignantForm, stagiaireForm,stageForm,organismeForm,membreForm,juryForm,conventionForm,ficheForm
from stage.models import Enseignant, stagiaire, Stage,OrganismeStage,Membre
from django.db.models import Q
# Create your views here.
   ######################## Enseignant
def index (request):
    Enseignants = Enseignant.objects.all()
    return render(request,'Liste_Enseignant.html',{'Enseignant':Enseignants}) 
def index2(request):
    stagiaires = stagiaire.objects.all()
    return render(request,'Liste_Stagiaire.html',{'stagiaire': stagiaires})
def index3 (request):
    stages = Stage.objects.all()
    return render(request,'Liste_Stage.html',{'Stage':stages})
def index4 (request):
    OrganismeStages = OrganismeStage.objects.all()
    return render(request,'Liste_Organismes.html',{'OrganismeStage':OrganismeStages})
def index5 (request):
    Membres = Membre.objects.all()
    return render(request,'Liste_Membre.html',{'Membre':Membres})

def recherche (request):
   # if request.method =='GET':
       # Enseignants=""
       # print()
        #print(query)
        #if query:
        search =request.GET.get('search')
        Enseignants=Enseignant.objects.filter(nomE__icontains= search) ,
                                              # Q(prenomE__icontains=search))
        context = {
            'Enseignants':Enseignants,
        }
        return render(request,'templates/Liste_Enseignant.html',context)
    
#inner_qs = Blog.objects.filter(name__contains='Cheddar')
   

def Ajouter_Enseignant(request):
    if request.method =='POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            form=EnseignantForm()
            mssg="Enseignant ajouté, vous pouvez saisir un autre"
           # return redirect_stderr("Liste_Enseignant")
            return render (request,"Ajouter_Enseignant.html",{"form":form,"message":mssg})
    else:
       form = EnseignantForm()
       Mssg = "veuillez remplir tous les champs"
       return render (request,"Ajouter_Enseignant.html",{"form":form,"message":Mssg})

def Ajouter_stagiaire(request):
    if request.method == "POST":
       form= stagiaireForm(data=request.Post)
       if form.is_valid():
           form.save()
           form=EnseignantForm()
           mssg="Stagiaire ajouté, vous pouvez saisir un autre"
           #return redirect_stderr("Liste_Stagiaire")
           return render (request,"Ajouter_Stagiaire.html",{"form":form,"message":mssg})

    else:
        form = stagiaireForm()
        Mssg = "veuillez remplir tous les champs"
        return render (request,"Ajouter_Stagiaire.html",{"form":form,"message":Mssg})
        return render(request,'stagiaire.html',{"form":form})

def Ajouter_Stage(request):
    if request.method == "POST":
       form= stageForm(data=request.Post)
       if form.is_valid():
           form.save()
           form=stageForm()
           mssg="Stage ajouté, vous pouvez saisir un autre"
           #return redirect_stderr("Liste_Stagiaire")
           return render (request,"Ajouter_Stage.html",{"form":form,"message":mssg})

    else:
        form = stageForm()
        Mssg = "veuillez remplir tous les champs"
        return render (request,"Ajouter_Stage.html",{"form":form,"message":Mssg})
        
def Ajouter_Organisme(request):
    if request.method == "POST":
       form= organismeForm(data=request.Post)
       if form.is_valid():
           form.save()
           form=organismeForm()
           mssg="Organisme ajouté, vous pouvez saisir un autre"
           return render (request,"Ajouter_Organisme.html",{"form":form,"message":mssg})

    else:
        form = organismeForm()
        Mssg = "veuillez remplir tous les champs"
        return render (request,"Ajouter_Organisme.html",{"form":form,"message":Mssg})

def Ajouter_Membre(request):
    if request.method == "POST":
       form=  membreForm(data=request.Post)
       if form.is_valid():
           form.save()
           form= membreForm()
           mssg="Membre ajouté, vous pouvez saisir un autre"
           return render (request,"Ajouter_Membre.html",{"form":form,"message":mssg})

    else:
        form =  membreForm()
        Mssg = "veuillez remplir tous les champs"
        return render (request,"Ajouter_Membre.html",{"form":form,"message":Mssg})
       
def Ajouter_Jury(request):
    if request.method == "POST":
       form=  juryForm(data=request.Post)
       if form.is_valid():
           form.save()
           form= juryForm()
           mssg="Jury ajouté, vous pouvez saisir un autre"
           return render (request,"Ajouter_Jury.html",{"form":form,"message":mssg})

    else:
        form =  juryForm()
        Mssg = "veuillez remplir tous les champs"
        return render (request,"Ajouter_Jury.html",{"form":form,"message":Mssg})
       
def Ajouter_Convention(request):
    if request.method == "POST":
       form=  conventionForm(data=request.Post)
       if form.is_valid():
           form.save()
           form= conventionForm()
           mssg="Convention ajouté, vous pouvez saisir un autre"
           return render (request,"Ajouter_Convention.html",{"form":form,"message":mssg})

    else:
        form =  conventionForm()
        Mssg = "veuillez remplir tous les champs"
        return render (request,"Ajouter_Convention.html",{"form":form,"message":Mssg})
       

def Ajouter_Fiche(request):
    if request.method == "POST":
       form=  ficheForm(data=request.Post)
       if form.is_valid():
           form.save()
           form= ficheForm()
           mssg="Fiche ajouté, vous pouvez saisir un autre"
           return render (request,"Ajouter_Fiche.html",{"form":form,"message":mssg})

    else:
        form =  ficheForm()
        Mssg = "veuillez remplir tous les champs"
        return render (request,"Ajouter_Fiche.html",{"form":form,"message":Mssg})
       



