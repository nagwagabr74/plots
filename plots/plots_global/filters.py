
import django_filters
from phonenumber_field.widgets import  PhoneNumberInternationalFallbackWidget
from .models import SpecificationUnitsData,Compound,Activities,Governerates,LandOperatingStatus
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit

class UnitsDataFilter(django_filters.FilterSet):
    CompoundId = django_filters.ModelChoiceFilter(queryset=Compound.objects.all(),label="اسم المجمع")
    GoverneratesId = django_filters.ModelChoiceFilter(queryset=Governerates.objects.all(),label="المحافظة")
    Main_Activity=django_filters.ModelMultipleChoiceFilter(queryset=Activities.objects.all(),help_text="يمكنك اختيار أكثر من منتج")
    LandOperatingStatus=django_filters.ModelChoiceFilter(queryset=LandOperatingStatus.objects.all(),help_text="يمكنك اختيار أكثر من منتج")
    SubActivity=django_filters.CharFilter(lookup_expr='icontains',label="النشاط الواقع")
    OwnerUnit = django_filters.CharFilter(lookup_expr='icontains',label="اسم المستثمر")
    UnitNumber=django_filters.BaseInFilter(lookup_expr='in',label="رقم السجل",help_text=" قم بادخال ارقام الوحدات مفصوله ب علامة الترقيم")
    class Meta:
        model = SpecificationUnitsData
        fields = ['GoverneratesId','CompoundId','UnitNumber','Main_Activity','LandOperatingStatus','SubActivity']
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     helper= FormHelper()
    #     helper.layout=Layout(
    #             HTML(' <h1 class="text-center text-info">إدخال وحدة</h1>'),
    #         )
    #     for field in self.Meta().fields:
    #         helper.layout.append(
    #             Field(field, wrapper_class='row')
    #             )
    #     helper.layout.append(Submit('submit', 'بحث', css_class='btn btn-info'))
    #     helper.field_class="col-lg-9 col-sm-12"
    #     helper.label_class="col-3"
    

    
