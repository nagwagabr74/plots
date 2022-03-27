from django.shortcuts import render
from .models import SpecificationUnitsData

# Create your views here.

def SpecificationUnitsData_list(request):
    specificationUnitsData = SpecificationUnitsData.objects.all()
    specificationUnitsData_list = []
    for unitdata in specificationUnitsData:
        specificationUnitsData_list.append({"specificationUnitsData": specificationUnitsData})
    context = {
        "SpecificationUnitsData_list": specificationUnitsData_list
    }
    return render(request, "plots_global/unitdata_list.html", context)



def home(request):
       
    context = {
        'unitdata': SpecificationUnitsData.objects.all()

    }
    return render(request, 'plots_global/home.html', context)

