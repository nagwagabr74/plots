
import django_filters
from phonenumber_field.widgets import  PhoneNumberInternationalFallbackWidget
from .models import SpecificationUnitsData,Compound,Activities,Governerates
from django import forms

class UnitsDataFilter(django_filters.FilterSet):
    CompoundId = django_filters.ModelChoiceFilter(queryset=Compound.objects.all(),label="اسم المجمع")
    GoverneratesId = django_filters.ModelChoiceFilter(queryset=Governerates.objects.all(),label="المحافظة")
    Main_Activity=django_filters.ModelMultipleChoiceFilter(queryset=Activities.objects.all(),help_text="يمكنك اختيار أكثر من منتج")
    # my__REGISTRY_NUMBER=django_filters.BaseInFilter(lookup_expr='in',label="رقم السجل",help_text=" قم بادخال ارقام السجل مفصوله ب علامة الترقيم")
    # CEO_NAME=django_filters.CharFilter(lookup_expr='icontains',label="اسم المدير")
    # DETAILED_ADDRESS=django_filters.CharFilter(lookup_expr='icontains',label=" العنوان",widget=forms.Textarea(attrs={'rows':2, 'cols':4}))
    # Prouducts=django_filters.ModelMultipleChoiceFilter(queryset=INDUSTRIAL_PRODUCTS.objects.all(),help_text="يمكنك اختيار أكثر من منتج")
    class Meta:
        model = SpecificationUnitsData
        fields = ['GoverneratesId','CompoundId','UnitNumber','Main_Activity']
        
    # def __init__(self, *args, **kwargs):
    #     super(FACILITY_DATAFilter, self).__init__(*args, **kwargs)
    #     # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
    #     if self.data == {}:
    #         self.queryset = self.queryset.none()

