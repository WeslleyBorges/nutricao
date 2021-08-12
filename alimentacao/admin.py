from django.contrib import admin
from django.contrib.admin import ModelAdmin

from alimentacao.models import Alimento, Medida, Refeicao, Porcao, TipoRefeicao


class PorcaoInline(admin.TabularInline):
    model = Porcao
    extra = 1
    max_num = 15


class RefeicaoAdmin(ModelAdmin):
    inlines = [
        PorcaoInline
    ]


admin.site.register(Alimento)
admin.site.register(Medida)
admin.site.register(TipoRefeicao)
admin.site.register(Porcao)
admin.site.register(Refeicao, RefeicaoAdmin)
