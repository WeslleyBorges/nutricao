from django.db import models
from django.db.models import Sum
from datetime import date
from django.apps import apps


class RefeicaoManager(models.Manager):
    def get_whole_day_info(self):
        today = date.today()
        refeicoes = self.filter(dia=today)

        Porcao = apps.get_model('alimentacao', 'Porcao')

        whole_day_info = Porcao.objects.filter(refeicao_alimento__in=refeicoes).aggregate(
            carboidratos=Sum('alimento__carboidratos'),
            proteinas=Sum('alimento__proteinas'),
            gorduras=Sum('alimento__gorduras')
        )

        return whole_day_info
