from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    jor1 = models.TimeField()
    jor2 = models.TimeField()
    jor3 = models.TimeField()
    jor4 = models.TimeField()

    def __str__(self):
        return self.nome

class Dado(models.Model):
    hostname = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    visto = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Sinal(models.Model):
    username = models.CharField(max_length=64)
    hostname = models.CharField(max_length=64)
    acao = models.CharField(max_length=64)
    hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

