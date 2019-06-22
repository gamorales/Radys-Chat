from django.db import models

class Usuarios(models.Model):
    email = models.EmailField(max_length=254)
    usuario = models.CharField(max_length=15)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.usuario


