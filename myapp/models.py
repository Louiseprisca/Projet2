from django.db import models

# Create your models here.

class Feature(models.Model):
    name = models.CharField(max_length=50, default='')
    details = models.CharField(max_length=255, default='')


class Client(models.Model):
        id_client = models.AutoField(primary_key=True)
        nom_client = models.CharField(max_length=100)
        prenom_client = models.CharField(max_length=100)
        destination_client = models.CharField(max_length=255)
        date_demande = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
             return f"{self.prenom_client} {self.nom_client}"

class Chauffeur(models.Model):
    id_chauffeur = models.AutoField(primary_key=True)
    nom_chauffeur = models.CharField(max_length=100)
    prenom_chauffeur = models.CharField(max_length=100)
    etat = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.prenom_chauffeur} {self.nom_chauffeur}"

class Vehicule(models.Model):
    id_vehicule = models.AutoField(primary_key=True)
    immatriculation = models.CharField(max_length=20)
    marque = models.CharField(max_length=100)
    
    def __str__(self):
        return self.immatriculation

class Voyage(models.Model):
    id_voyage = models.AutoField(primary_key=True)
    heure_depart = models.DateTimeField()
    heure_arriver = models.DateTimeField()
    id_classe = models.CharField(max_length=50)  # À définir selon les options
    id_chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE)
    id_vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Voyage {self.id_voyage} de {self.heure_depart} à {self.heure_arriver}"

class Colis(models.Model):
    id_bagage = models.AutoField(primary_key=True)
    libele = models.CharField(max_length=255)
    prix_colis = models.DecimalField(max_digits=10, decimal_places=2)
    masse = models.FloatField()
    emetteur = models.CharField(max_length=255)
    destinataire = models.CharField(max_length=255)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.libele

class Message(models.Model):
    id_colis = models.ForeignKey(Colis, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    date_reception = models.DateTimeField(null=True, blank=True)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Message pour colis {self.id_colis}"

class Avis(models.Model):
    id_avis = models.AutoField(primary_key=True)
    contenu = models.TextField()
    date_avis = models.DateTimeField(auto_now_add=True)
    heure_avis = models.TimeField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Avis de {self.id_client}"

class Réserver(models.Model):
    statut_réserv = models.CharField(max_length=50)
    date_réserv = models.DateField()
    heure_réserv = models.TimeField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)

    def __str__(self):
        return f"Réservation pour {self.id_client} sur le voyage {self.id_voyage}"

class Compte(models.Model):
    id_compte = models.AutoField(primary_key=True)
    login = models.CharField(max_length=100, unique=True)
    mot_passe = models.CharField(max_length=100)
    
    def __str__(self):
        return self.login