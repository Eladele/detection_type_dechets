from django.db import models

class Dechets(models.Model):
    Type_dechet = models.CharField(max_length=50)
    Description = models.TextField()
    Date_ajout = models.DateField()
    Etat = models.CharField(max_length=50)

class Points_de_collecte(models.Model):
    Nom_point_collecte = models.CharField(max_length=100)
    Adresse = models.TextField()
    Type_dechets_acceptes = models.CharField(max_length=100)
    Capacite_stockage = models.IntegerField()

class Collectes(models.Model):
    ID_point_collecte = models.ForeignKey(Points_de_collecte, on_delete=models.CASCADE)
    Date_collecte = models.DateField()
    Poids_total_collecte = models.DecimalField(max_digits=10, decimal_places=2)
    Type_dechets_collectes = models.CharField(max_length=100)

class Traitement(models.Model):
    ID_dechet = models.ForeignKey(Dechets, on_delete=models.CASCADE)
    Type_traitement = models.CharField(max_length=100)
    Date_traitement = models.DateField()
    Destination_traitement = models.CharField(max_length=100)

class Fournisseurs_de_services(models.Model):
    Nom_entreprise = models.CharField(max_length=100)
    Adresse = models.TextField()
    Type_service_offert = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)

