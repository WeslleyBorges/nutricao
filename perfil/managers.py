from django.db.models import Manager


class PerfilManager(Manager):
    def get_taxa_metabolismo_basal(self):
        perfil = self.first()
        tmb = int(66 + (13.8 * perfil.massa) + (5 * perfil.altura) - (6.8 * perfil.idade))
        return tmb
