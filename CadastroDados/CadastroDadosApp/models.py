from django.db import models

# Create your models here.
class Dados(models.Model):
    
    nome = models.CharField(max_length=50)
    idade = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Dado'
        verbose_name_plural = 'Dados'