from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bandname_id>/', views.bandid, name='detail'),
    # ex: /polls/5/results/
    path('<int:bandname_id>/bandname/', views.bandname, name='bandname'),
]