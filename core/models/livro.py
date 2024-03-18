from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    

    def __str__(self):
        return self.titulo