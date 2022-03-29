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

# Create your views here.

class UnitListView(LoginRequiredMixin,ListView):
    model=SpecificationUnitsData
    template_name="plots_global/unitdata_list.html"
    queryset=SpecificationUnitsData.objects.all()
    
 