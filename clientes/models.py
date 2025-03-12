from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(verbose_name='nombre del cliente',max_length=50,unique=True)
    telefono = models.CharField(verbose_name='telefono',max_length=11)
    numeros = models.JSONField(verbose_name='numeros jugados',default=list)
    estado = models.BooleanField(verbose_name='estado',default=False)
    abono = models.DecimalField(verbose_name='Abono', decimal_places=2, max_digits=12,default=0.00)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['fecha_registro']
    def __str__(self):
        return self.nombre