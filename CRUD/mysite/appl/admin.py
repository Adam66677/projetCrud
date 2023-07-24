from django.contrib import admin
from openpyxl import Workbook
from django.http import HttpResponse



# Register your models here.

from appl.models import Ville 
from appl.models import Arrondissement 
from appl.models import Axe 
from appl.models import Armoire 
from appl.models import Depart 
from appl.models import Support
from appl.models import Luminaire
from appl.models import ModeleSupport 
from appl.models import ModeleLuminaire 
from appl.models import AnomalieArmoire
from appl.models import AnomaliePl


@admin.register(Ville)
class VilleAdmin(admin.ModelAdmin):
    search_fields = ['code_ville']
    list_filter = ['nom_ville']



@admin.register(Arrondissement)
class ArrondissementAdmin(admin.ModelAdmin):
    list_display = ['code_district','nom_district']
    search_fields = ['code_district']
    list_filter = ['ville']


@admin.register(Axe)
class AxeAdmin(admin.ModelAdmin):
    list_display = ['code_axe','nom_axe']
    search_fields = ['code_axe','nom_axe']
    list_filter = ['type_axe','arrondissement']


@admin.register(Armoire)
class Armoire(admin.ModelAdmin):
    list_display = ['code_armoire']
    search_fields = ['code_armoire']
    list_filter = ['axe__nom_axe','axe__arrondissement__nom_district']
    actions = ['export_to_excel']
    
    
    def export_to_excel(self, request, queryset):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=extraction.xlsx'

        workbook = Workbook()
        worksheet = workbook.active

        # Ajouter les en-têtes de colonnes
        worksheet.append(['code_armoire', 'nom_axe', 'nom_arrondissement'])

        for armoire in queryset:
            worksheet.append([armoire.code_armoire, armoire.axe.nom_axe, armoire.axe.arrondissement.nom_district])

        workbook.save(response)
        return response

    export_to_excel.short_description = "Export to Excel"


@admin.register(Depart)
class Depart(admin.ModelAdmin):
    search_fields = ['code_depart']
    list_filter = ['armoire']


@admin.register(Support)
class Support(admin.ModelAdmin):
    list_display = ['id_support']
    search_fields = ['id_support']
    list_filter = ['dÚpart','nom_axe__nom_axe','modele_support']
    actions = ['export_to_excel']

    def export_to_excel1(self, request, queryset):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=extraction.xlsx'

        workbook = Workbook()
        worksheet = workbook.active

        # Ajouter les en-têtes de colonnes
        worksheet.append(['id_support', 'nom_axe', 'nom_arrondissement'])

        for support in queryset:
            worksheet.append([support.id_support, support.axe.nom_axe, support.axe.arrondissement.nom_district])

        workbook.save(response)
        return response

    export_to_excel1.short_description = "Export to Excel"

@admin.register(Luminaire)
class Luminaire(admin.ModelAdmin):
    search_fields = ['id_luminaire']
    list_filter = ['id_support','id_modele_luminaire']


@admin.register(ModeleSupport)
class ModeleSupport(admin.ModelAdmin):
    search_fields = ['id_modele_support']
    
@admin.register(ModeleLuminaire)
class ModeleLuminaire(admin.ModelAdmin):
    search_fields = ['id_modele_luminaire']
    
@admin.register(AnomalieArmoire)
class AnomalieArmoire(admin.ModelAdmin):
    search_fields = ['id_anomalie_cm']   
    list_filter = ['code_armoire'] 

@admin.register(AnomaliePl)
class AnomaliePl(admin.ModelAdmin):
    search_fields = ['id_anomalie_pl']
    list_filter = ['id_luminaire']

