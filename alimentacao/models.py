from django.db import models


# Create your models here.
class Medida(models.Model):
    descricao = models.CharField(max_length=30)
    abreviacao = models.CharField(max_length=5)

    def __str__(self):
        return self.descricao


class TipoRefeicao(models.Model):
    descricao = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'tipos de refeições'

    def __str__(self):
        return self.descricao


class Alimento(models.Model):
    descricao = models.CharField(max_length=50)
    kcal = models.IntegerField()
    carboidratos = models.DecimalField(max_digits=4, decimal_places=1)
    proteinas = models.DecimalField(max_digits=4, decimal_places=1)
    gorduras = models.DecimalField(max_digits=4, decimal_places=1)
    quantidade = models.IntegerField()
    medida = models.ForeignKey(Medida, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.descricao


class Refeicao(models.Model):
    tipo_refeicao = models.ForeignKey(TipoRefeicao, on_delete=models.DO_NOTHING)
    dia = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'refeições'

    def __str__(self):
        return f'{self.tipo_refeicao} ({self.dia})'


class Porcao(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    refeicao_alimento = models.ForeignKey(Refeicao, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'porções'

    def __str__(self):
        return self.alimento.descricao
