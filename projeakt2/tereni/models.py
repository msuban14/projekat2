from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tereni(models.Model):
    naziv=models.CharField(max_length=200)
    mesto=models.CharField(max_length=200)
    tip=models.CharField(max_length=100)
    naziv_vode=models.CharField(max_length=200)
    korisnikVode=models.CharField(max_length=200,default="")
    tip_dozvole=models.CharField(max_length=200)
    latituda=models.DecimalField(max_digits=10,decimal_places=8)
    longituda = models.DecimalField(max_digits=11, decimal_places=8)
    opis = models.TextField(max_length=500,default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    #korisnik = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv

class Ocene(models.Model):
    ocena = models.IntegerField()
    #relacija
    teren = models.ForeignKey(Tereni, on_delete=models.CASCADE)
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    #korisnik = models.ForeignKey(User, on_delete=models.CASCADE)

class Komentari(models.Model):
    sadrzaj = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #relacija
    teren = models.ForeignKey(Tereni,on_delete=models.CASCADE)
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    #korisnik = models.ForeignKey(User, on_delete=models.CASCADE)



