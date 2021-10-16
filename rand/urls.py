from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jumble/', views.jumble),
    path('album/', views.albums),
    path('search/', views.SearchResultsView)
]
