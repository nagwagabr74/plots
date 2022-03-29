
from django.urls import path
from . import views

urlpatterns = [

    # path('', views.home, name='home'),
    path('', views.UnitListView.as_view(), name='UnitsData'),
    path('search', views.UnitsDataFilter.as_view(), name='search'),
    
]