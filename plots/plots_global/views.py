from django.shortcuts import render
from .models import SpecificationUnitsData
from django.views.generic import (
CreateView,
DetailView,
ListView,
DeleteView,
UpdateView,
FormView
)
from  django.views.generic.detail import  SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2.views import SingleTableView
from django_tables2.export.views import ExportMixin
from django_filters.views import FilterView

from .filters import UnitsDataFilter

# Create your views here.

class UnitListView(LoginRequiredMixin,ListView):
    model=SpecificationUnitsData
    template_name="plots_global/unitdata_list.html"
    queryset=SpecificationUnitsData.objects.all()

class UnitsDataFilter(FilterView,ExportMixin,SingleTableView):
        model =SpecificationUnitsData
        filterset_class = UnitsDataFilter
        #context_object_name = 'users'  # Default: object_list
   
    
 