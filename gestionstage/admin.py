from django.contrib import admin
from .models import Convention, Ficheeva, OrganismeStage,Jury,Enseignant,Membre, Rapport, Stage, stagiaire
# Register your models here.
admin.site.register(OrganismeStage)
admin.site.register(Jury)
admin.site.register(Enseignant)
admin.site.register(Membre)
admin.site.register(stagiaire)
admin.site.register(Rapport)
admin.site.register(Stage)
admin.site.register(Convention)
admin.site.register(Ficheeva)


