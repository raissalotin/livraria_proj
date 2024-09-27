from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"



    def __str__(self):
        return self.name