from django.contrib import admin
from django.views.decorators.cache import never_cache

from alimentacao.models import Alimento, Medida, Refeicao, Porcao, TipoRefeicao


class CustomAdminSite(admin.AdminSite):
    @never_cache
    def index(self, request, extra_context=None):
        extra_context = Refeicao.objects.get_whole_day_info()
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


custom_admin_site = CustomAdminSite()

custom_admin_site.register(Alimento)
custom_admin_site.register(Medida)
custom_admin_site.register(TipoRefeicao)
custom_admin_site.register(Refeicao, RefeicaoAdmin)
