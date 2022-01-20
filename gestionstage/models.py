from contextlib import nullcontext
from dataclasses import dataclass
from datetime import date
from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
 

# Create your models here.
class OrganismeStage (models.Model):
    nomOrganisme = models.CharField(max_length=20,null=False)
    adresse = models.CharField(max_length=40,null=False)
    email = models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.nomOrganisme

class Jury(models.Model):
    codeJ = models.TextField(max_length=15)
    dateSoutenance = models.DateField(default="01/01/2022")
    def __str__(self):
        return (self.codeJ)
       

class Enseignant(models.Model):
    nomE = models.CharField(max_length=20,null=False)
    prenomE = models.CharField(max_length=20,null=False)
    grade = models.CharField(max_length=2,null=False)
    codeJ = models.ForeignKey(Jury, on_delete=models.SET_NULL, null= True, blank=True )
    def __str__(self):
        return (self.nomE+"\t"+self.prenomE)
    

class Stage(models.Model):
    titreStage = models.CharField(max_length=40)
    class ts(models.TextChoices):
        CP1 = '1CP',_('Stage ouvrier 1CP')
        CS1 = '1CS',_('Stage technique 1CS')
        CS3 = 'PFE3CS',_('Stage technique PFE 3CS')
    typeStage = models.CharField(max_length=20, choices=ts.choices)
    enseignant = models.ForeignKey(Enseignant,on_delete=models.CASCADE)
    #stagiaire = models.ManyToManyField(stagiaire,related_name='stagiaire')
    #rapport =  models.ManyToManyField(Rapport,related_name='rapport')
    #rapport = models.ForeignKey(Rapport,on_delete=models.SET_NULL, null= False, blank=False )
    jury = models.ForeignKey(Jury,on_delete=models.SET_NULL, null= True, blank=True )
    organisme = models.ForeignKey(OrganismeStage, on_delete=models.CASCADE )
    def __str__(self):
        return (self.titreStage+"\t"+self.typeStage+"\t"+self.enseignant.nomE+"\t"+self.organisme.nomOrganisme)
           
class Rapport(models.Model):
    nbrpages = models.IntegerField()
    stage = models.ForeignKey(Stage,on_delete=models.SET_NULL, null= True, blank=False )
    #stage = models.OneToOneField(Stage, null=True, on_delete=models.CASCADE)
    #stage = models.ManyToManyField(Stage,related_name='stage')s
    def __int__(self):
        return (self.nbrpages)
    def __str__(self):
        return (self.stage.titreStage)
           
class Membre(models.Model):
    nomM = models.CharField(max_length=20)
    prenomM = models.CharField(max_length=20)
    poste = models.CharField(max_length=20)
    codeJ = models.ForeignKey(Jury, on_delete=models.SET_NULL, null= True, blank=True )
    organisme = models.ForeignKey(OrganismeStage, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage,on_delete=models.SET_NULL, null= True, blank=True )
    def __str__(self):
        return (self.nomM+"\t"+self.prenomM)

class stagiaire (models.Model):
    noms = models.CharField(max_length=40, null= False)
    prenoms = models.CharField(max_length=40, null= False)
    DateNaissance = models.DateField(null= False)
    Email = models.EmailField(max_length = 254, null= False)
    annedEude = models.IntegerField(default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null= True, blank=True )
    def __str__(self):
        return (self.noms+"\t"+self.prenoms+"\t"+self.stage.titreStage)

class Convention(models.Model):
    duree = models.CharField(max_length=2)
    stage = models.ForeignKey(Stage,on_delete=models.CASCADE )
    def __str__(self):
        return (self.duree)
    def __str__(self):
        return(self.stage.titreStage)
    

class Ficheeva(models.Model):
    noteava = models.IntegerField(default=0, validators=[
            MaxValueValidator(20),
            MinValueValidator(0)])
    stage = models.ForeignKey(Stage,on_delete=models.CASCADE )

    def __float__(self):
        return(self.noteava)

    
 