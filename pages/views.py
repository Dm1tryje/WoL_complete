from calendar import c
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'mainPages/home.html'

class tournamentPage(TemplateView):
    template_name = 'mainPages/tournament.html'

class racePage(TemplateView):
    template_name = 'mainPages/race.html'

class fractionPage(TemplateView):
    template_name = 'mainPages/fraction.html'

class gameWorldPage(TemplateView):
    template_name = 'mainPages/game_world.html'

class downloadPage(TemplateView):
    template_name = 'mainPages/download.html'

class allienceDetailPage(TemplateView):
    template_name = 'mainPages/allience_detail.html'

class hordeDetailPage(TemplateView):
    template_name = 'mainPages/horde_detail.html'

class renegadesDetailPage(TemplateView):
    template_name = 'mainPages/renegades_detail.html'