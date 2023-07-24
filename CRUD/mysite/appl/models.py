# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Ville(models.Model):
    code_ville = models.CharField(db_column='Code_Ville', primary_key=True, max_length=3, db_collation='French_CI_AS')  # Field name made lowercase.
    nom_ville = models.CharField(db_column='Nom_Ville', max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ville'


class Arrondissement(models.Model):
    code_district = models.CharField(db_column='Code_District', primary_key=True, max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    nom_district = models.CharField(db_column='Nom_District', max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    ville = models.ForeignKey(Ville, models.DO_NOTHING, db_column='Ville')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Arrondissement'

class Axe(models.Model):
    code_axe = models.CharField(db_column='Code_Axe', primary_key=True, max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    nom_axe = models.CharField(db_column='Nom_Axe', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_axe = models.CharField(db_column='Type_Axe', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    arrondissement = models.ForeignKey(Arrondissement, models.DO_NOTHING, db_column='Arrondissement', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Axe'

class Armoire(models.Model):
    code_armoire = models.CharField(db_column='Code_Armoire', primary_key=True, max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    designation_poste = models.CharField(db_column='Designation_Poste', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    axe = models.ForeignKey(Axe, models.DO_NOTHING, db_column='Axe', blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=11, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    x_geomÚtrie = models.CharField(db_column='X_Geométrie', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    numero_compteur = models.CharField(db_column='Numero_Compteur', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    implantation_compteur = models.CharField(db_column='Implantation_Compteur', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hierarchie = models.CharField(db_column='Hierarchie', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mode_pose = models.CharField(db_column='Mode_Pose', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_alimentation = models.CharField(db_column='Type_Alimentation', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    section_arrivee = models.CharField(db_column='Section_Arrivee', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombre_departs = models.IntegerField(db_column='Nombre_Departs', blank=True, null=True)  # Field name made lowercase.
    type_protection = models.CharField(db_column='Type_Protection', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    calibre_protection = models.CharField(db_column='Calibre_Protection', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mode_allumage = models.CharField(db_column='Mode_Allumage', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telegestion = models.CharField(db_column='Telegestion', max_length=3, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mise_terre = models.CharField(db_column='Mise_Terre', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    resistance_terre = models.CharField(db_column='Resistance_Terre', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_manoeuvre = models.CharField(db_column='Type_Manoeuvre', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hauteur = models.FloatField(db_column='Hauteur', blank=True, null=True)  # Field name made lowercase.
    largeur = models.FloatField(db_column='Largeur', blank=True, null=True)  # Field name made lowercase.
    profondeur = models.FloatField(db_column='Profondeur', blank=True, null=True)  # Field name made lowercase.
    etat = models.CharField(db_column='Etat', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image1 = models.CharField(db_column='Image1', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image2 = models.CharField(db_column='Image2', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image3 = models.CharField(db_column='Image3', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image4 = models.CharField(db_column='Image4', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image5 = models.CharField(db_column='Image5', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image6 = models.CharField(db_column='Image6', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image7 = models.CharField(db_column='Image7', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image8 = models.CharField(db_column='Image8', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Armoire'

class Depart(models.Model):
    id_depart = models.CharField(db_column='ID_Depart', primary_key=True, max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    nom_depart = models.CharField(db_column='Nom_Depart', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_depart = models.CharField(db_column='Type_Depart', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_protection = models.CharField(db_column='Type_Protection', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    calibre = models.CharField(db_column='Calibre', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tension = models.FloatField(db_column='Tension', blank=True, null=True)  # Field name made lowercase.
    type_cable = models.CharField(db_column='Type_Cable', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    section_cable = models.CharField(db_column='Section_Cable', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cheminement = models.CharField(db_column='Cheminement', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    armoire = models.ForeignKey(Armoire, models.DO_NOTHING, db_column='Armoire', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Depart'

class ModeleSupport(models.Model):
    id_modele_support = models.IntegerField(db_column='ID_modele_support', primary_key=True)  # Field name made lowercase.
    nom_modele_support = models.CharField(db_column='Nom_modele_support', max_length=10, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_eclairage = models.CharField(db_column='Type_Eclairage', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_support = models.CharField(db_column='Type_support', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_ancrage = models.CharField(db_column='Type_ancrage', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matÚriau_support = models.CharField(db_column='Matériau_support', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nom_commercial = models.CharField(db_column='Nom_commercial', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hauteur_support = models.FloatField(db_column='Hauteur_support', blank=True, null=True)  # Field name made lowercase.
    nb_luminaire_par_sup = models.IntegerField(db_column='Nb_luminaire_par_sup', blank=True, null=True)  # Field name made lowercase.
    avancÚe = models.CharField(db_column='Avancée', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=100, db_collation='French_CI_AS', blank=True, null=True)
    plan_dessin = models.CharField(db_column='Plan_dessin', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Modele_support'


class Support(models.Model):
    id_support = models.CharField(db_column='ID_support', primary_key=True, max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    nom_axe = models.ForeignKey(Axe, models.DO_NOTHING, db_column='Nom_Axe', blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=11, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    dÚpart = models.ForeignKey(Depart, models.DO_NOTHING, db_column='Départ', blank=True, null=True)  # Field name made lowercase.
    modele_support = models.ForeignKey(ModeleSupport, models.DO_NOTHING, db_column='Modele_support', blank=True, null=True)  # Field name made lowercase.
    etat_general = models.CharField(db_column='Etat_general', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    section_cable = models.CharField(db_column='Section_cable', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image1 = models.CharField(max_length=100, db_collation='French_CI_AS', blank=True, null=True)
    image2 = models.CharField(max_length=100, db_collation='French_CI_AS', blank=True, null=True)
    image3 = models.CharField(max_length=100, db_collation='French_CI_AS', blank=True, null=True)
    image4 = models.CharField(max_length=100, db_collation='French_CI_AS', blank=True, null=True)
    type_cable_alimentation = models.CharField(db_column='Type_cable_alimentation', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_raccordement = models.CharField(db_column='Type_raccordement', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    protection_surintensites = models.CharField(db_column='Protection_surintensites', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Support'

class ModeleLuminaire(models.Model):
    id_modele_luminaire = models.IntegerField(db_column='ID_Modele_luminaire', primary_key=True)  # Field name made lowercase.
    nom_modele_luminaire = models.CharField(db_column='Nom_modele_luminaire', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    alias1 = models.CharField(db_column='Alias1', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    alias2 = models.CharField(db_column='Alias2', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_luminaire = models.CharField(db_column='Type_luminaire', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hauteur = models.FloatField(db_column='Hauteur', blank=True, null=True)  # Field name made lowercase.
    marque = models.CharField(db_column='Marque', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nom_commercial = models.CharField(db_column='Nom_commercial', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    puissance_lampe = models.FloatField(db_column='Puissance_lampe', blank=True, null=True)  # Field name made lowercase.
    puissance_equipement = models.FloatField(db_column='Puissance_equipement', blank=True, null=True)  # Field name made lowercase.
    tension = models.FloatField(db_column='Tension', blank=True, null=True)  # Field name made lowercase.
    type_lampe = models.CharField(db_column='Type_lampe', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tempÚrature_couleur = models.FloatField(db_column='Température_couleur', blank=True, null=True)  # Field name made lowercase.
    type_Úquipement = models.CharField(db_column='Type_équipement', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reference_equipement = models.CharField(db_column='Reference_equipement', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_vasque = models.CharField(db_column='Type_vasque', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    protection_surintensites = models.CharField(db_column='Protection_surintensites', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    optique_luminaire = models.CharField(db_column='Optique_luminaire', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inclinaison = models.CharField(db_column='Inclinaison', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_cable = models.CharField(db_column='Type_cable', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    section_cable = models.FloatField(db_column='Section_cable', blank=True, null=True)  # Field name made lowercase.
    type_raccordement = models.CharField(db_column='Type_raccordement', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image1 = models.CharField(max_length=100, db_collation='French_CI_AS', blank=True, null=True)
    reflecteur = models.CharField(db_column='Reflecteur', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Modele_luminaire'


class Luminaire(models.Model):
    id_luminaire = models.CharField(db_column='ID_Luminaire', primary_key=True, max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    id_support = models.ForeignKey(Support, models.DO_NOTHING, db_column='ID_Support', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_modele_luminaire = models.ForeignKey(ModeleLuminaire, models.DO_NOTHING, db_column='ID_Modele_Luminaire', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Luminaire'


class AnomalieArmoire(models.Model):
    id_anomalie_cm = models.IntegerField(db_column='ID_Anomalie_CM', primary_key=True)  # Field name made lowercase.
    date_heure_visite = models.DateTimeField(db_column='Date_heure_visite', blank=True, null=True)  # Field name made lowercase.
    opÚrateur = models.CharField(db_column='Opérateur', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    commentaire = models.CharField(db_column='Commentaire', max_length=300, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=100, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    etat = models.CharField(db_column='Etat', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    etat1 = models.CharField(db_column='Etat1', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ponctuation = models.IntegerField(db_column='Ponctuation', blank=True, null=True)  # Field name made lowercase.
    code_armoire = models.ForeignKey(Armoire, models.DO_NOTHING, db_column='Code_Armoire', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anomalie_Armoire'


class AnomaliePl(models.Model):
    id_anomalie_pl = models.IntegerField(db_column='ID_Anomalie_PL', primary_key=True)  # Field name made lowercase.
    id_luminaire = models.ForeignKey(Luminaire, models.DO_NOTHING, db_column='ID_luminaire', blank=True, null=True)  # Field name made lowercase.
    date_heure_visite = models.DateTimeField(db_column='Date_heure_visite', blank=True, null=True)  # Field name made lowercase.
    opÚrateur = models.CharField(db_column='Opérateur', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    commentaire = models.CharField(db_column='Commentaire', max_length=200, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=100, db_collation='French_CI_AS', blank=True, null=True)
    options = models.CharField(db_column='Options', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    etat = models.CharField(db_column='Etat', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ponctuation = models.IntegerField(db_column='Ponctuation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anomalie_PL'























