from django.db.models import fields
from django import forms
from .models import Convention, Enseignant, Ficheeva, Jury, Membre, OrganismeStage, Stage, stagiaire
class EnseignantForm (forms.ModelForm):
    
    class Meta:
        model = Enseignant
        fields = "__all__"

class stagiaireForm (forms.ModelForm):
    
    class Meta:
        model = stagiaire
        fields = "__all__"

class stageForm (forms.ModelForm):
    
    class Meta:
        model = Stage
        fields = "__all__"

class organismeForm (forms.ModelForm):
    
    class Meta:
        model = OrganismeStage
        fields = "__all__"
        
class membreForm (forms.ModelForm):
    
    class Meta:
        model = Membre
        fields = "__all__"
        
class juryForm (forms.ModelForm):
    
    class Meta:
        model = Jury
        fields = "__all__"   
             
class conventionForm (forms.ModelForm):
    
    class Meta:
        model = Convention
        fields = "__all__"   
             
class ficheForm (forms.ModelForm):
    
    class Meta:
        model = Ficheeva
        fields = "__all__"