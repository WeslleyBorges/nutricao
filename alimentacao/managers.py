from django.db import models
from django.db.models import Sum, F
from datetime import date
from django.apps import apps


class RefeicaoManager(models.Manager):
    def get_whole_day_info(self):
        today = date.today()
        refeicoes = self.filter(dia=today)

        Porcao = apps.get_model('alimentacao', 'Porcao')

        multiplication_factor_expression = F('quantidade') / F('alimento__quantidade')

        whole_day_info = Porcao.objects.filter(refeicao_alimento__in=refeicoes).aggregate(
            kcal=Sum(F('alimento__kcal') * multiplication_factor_expression),
            carboidratos=Sum(F('alimento__carboidratos') * multiplication_factor_expression),
            proteinas=Sum(F('alimento__proteinas') * multiplication_factor_expression),
            gorduras=Sum(F('alimento__gorduras') * multiplication_factor_expression)
        )

        return whole_day_info
