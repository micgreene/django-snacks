from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class DBHomePageView(TemplateView):
  template_name = 'db_home.html'

class SaiyansPageView(TemplateView):
  template_name = 'saiyans.html'

class HumansPageView(TemplateView):
  template_name = 'humans.html'

class BulmaPageView(TemplateView):
  template_name = 'bulma.html'

class ChiChiPageView(TemplateView):
  template_name = 'chichi.html'

class KrillinPageView(TemplateView):
  template_name = 'krillin.html'

class RoshiPageView(TemplateView):
  template_name = 'roshi.html'

class TienPageView(TemplateView):
  template_name = 'tien.html'

class YamchaPageView(TemplateView):
  template_name = 'yamcha.html'

class GohanPageView(TemplateView):
  template_name = 'gohan.html'

class GokuPageView(TemplateView):
  template_name = 'goku.html'

class VegetaPageView(TemplateView):
  template_name = 'vegeta.html'
