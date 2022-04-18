from django.urls import path,re_path

from . import views
from .views import EletronicsView, eletronics

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^\d+', views.detail, name='detail'),
    re_path(r'^eletronics', views.eletronics, name='eletronics'),
    re_path(r'^eletronics', EletronicsView.as_view(), name='eletronics')
]