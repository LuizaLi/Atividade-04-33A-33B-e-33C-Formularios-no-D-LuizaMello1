from django.db import models

# Create your models here.
class Vantagens(models.Model):
  title = models.CharField(max_length=50)
  argumento = models.CharField(max_length=70)
  UTILIDADEV = [
    ("MU","Muitoutil"),
    ("L","Legal"),
    ("TF","Tantofaz"),
  ]
  vanttrabalho = models.CharField(max_length=70, choices=UTILIDADEV)
  vantlazer = models.CharField(max_length=70)

class Desvantagens(models.Model):
  title = models.CharField(max_length=50)
  UTILIDADED = [
    ("I","Impossivel"),
    ("A","Atrapalha"),
    ("NL","Naoligo"),
  ]
  argumento = models.CharField(max_length=70)
  desvpessoais = models.CharField(max_length=70)
  desvtrabalho = models.CharField(max_length=70, choices=UTILIDADED)

class Tabela(models.Model):
  title = models.CharField(max_length=50)
  coluna2 = models.CharField(max_length=50)