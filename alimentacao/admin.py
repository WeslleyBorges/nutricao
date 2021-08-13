from django.contrib import admin
from django.views.decorators.cache import never_cache
from datetime import date

from alimentacao.models import Alimento, Medida, Refeicao, Porcao, TipoRefeicao
from perfil.models import Perfil


class CustomAdminSite(admin.AdminSite):
    @never_cache
    def index(self, request, extra_context=None):
        whole_day_info = Refeicao.objects.get_whole_day_info()
        tmb = Perfil.objects.get_taxa_metabolismo_basal()
        extra_context = {
            **whole_day_info,
            'tmb': tmb
        }
        template_response = super().index(request, extra_context=extra_context)
        return template_response


class PorcaoInline(admin.TabularInline):
    model = Porcao
    extra = 1
    max_num = 15


class RefeicaoAdmin(admin.ModelAdmin):
    inlines = [
        PorcaoInline
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        today = date.today()
        return qs.filter(dia=today)


custom_admin_site = CustomAdminSite()

custom_admin_site.register(Alimento)
custom_admin_site.register(Medida)
custom_admin_site.register(TipoRefeicao)
custom_admin_site.register(Refeicao, RefeicaoAdmin)
custom_admin_site.register(Perfil)
