from django.db import models

# Create your models here.



class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    criador_dispositivo_nome = models.CharField(max_length=100,blank=True, null=True)
    class Meta:
        verbose_name = ("pessoa")
        verbose_name_plural = ("pessoas")

    def __str__(self):
        return self.nome


class Produto(models.Model):
    VARIEDADES = 1
    COMIDA = 2
    BRINQUEDO = 3
    PRODUTO_TIPO = {
        (VARIEDADES,'Variedades'),
        (COMIDA,'Comida'),
        (BRINQUEDO,'Brinquedo'),
    }
    nome = models.CharField(max_length=100)
    adicionado_em = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    codigo_produto = models.CharField(max_length=30, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(blank=True, null=True)
    categoria_tipo = models.PositiveSmallIntegerField(choices=PRODUTO_TIPO, blank=True, null=True)

    class Meta:
        verbose_name = ("produto")
        verbose_name_plural = ("produtos")

    def __str__(self):
        return self.nome
