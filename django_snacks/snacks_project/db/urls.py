from django.urls import path
from . import views
# from .views import HumansPageView
# from .views import SaiyansPageView

urlpatterns = [
  path('', views.DBHomePageView.as_view(), name = 'db_home'),
  path('humans/', views.HumansPageView.as_view(), name = 'humans'),
  path('saiyans/', views.SaiyansPageView.as_view(), name = 'saiyans'),
  path('bulma/', views.BulmaPageView.as_view(), name = 'bulma'),
  path('chichi/', views.ChiChiPageView.as_view(), name = 'chichi'),
  path('krillin/', views.KrillinPageView.as_view(), name = 'krillin'),
  path('roshi/', views.RoshiPageView.as_view(), name = 'roshi'),
  path('tien/', views.TienPageView.as_view(), name = 'tien'),
  path('yamcha/', views.YamchaPageView.as_view(), name = 'yamcha'),
  path('gohan/', views.GohanPageView.as_view(), name = 'gohan'),
  path('goku/', views.GokuPageView.as_view(), name = 'goku'),
  path('vegeta/', views.VegetaPageView.as_view(), name = 'vegeta'),
]