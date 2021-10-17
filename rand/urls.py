from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jumble/', views.jumble),
    path('album/', views.albums),
    path('results/', views.SearchResultsView.as_view(), name='search_results'),
    path('search/', SearchPageView.as_view(), name='search')
]
