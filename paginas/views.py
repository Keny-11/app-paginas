from django.views.generic import TemplateView


class VistaPaginaDeInicio(TemplateView):
    template_name = 'pagina de inicio.html'

class VistaPaginaAcercaDe(TemplateView):
    template_name = 'acerca de.html'
