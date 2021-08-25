from django.db import models
from django.db.models import Sum, F, ExpressionWrapper, FloatField, Func
from datetime import date
from django.apps import apps


class RefeicaoManager(models.Manager):
    def get_whole_day_info(self):
        today = date.today()
        refeicoes = self.filter(dia=today)

        Porcao = apps.get_model('alimentacao', 'Porcao')

        template = '%(function)s(%(expressions)s AS FLOAT)'

        quantidade_porcao = Func(F('quantidade'), function='CAST', template=template)
        quantidade_alimento = Func(F('alimento__quantidade'), function='CAST', template=template)

        multiplication_factor_expression = ExpressionWrapper(quantidade_porcao / quantidade_alimento,
                                                             output_field=FloatField())

        whole_day_info = Porcao.objects.filter(refeicao_alimento__in=refeicoes).aggregate(
            kcal=Sum(F('alimento__kcal') * multiplication_factor_expression),
            carboidratos=Sum(F('alimento__carboidratos') * multiplication_factor_expression, output_field=FloatField()),
            proteinas=Sum(F('alimento__proteinas') * multiplication_factor_expression, output_field=FloatField()),
            gorduras=Sum(F('alimento__gorduras') * multiplication_factor_expression, output_field=FloatField())
        )

        return whole_day_info
