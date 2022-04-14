from django import forms

from .models import SpecificationUnitsData,Governerates, Compound
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field,HTML,Submit



class Chart_unitStatusFormModel(forms.ModelForm):
    class Meta:
       
        model = Compound
        
        
        fields = ["CompoundName"]

   
    
    CompoundName= forms.ModelChoiceField(label='اختر المجمع ',required=False, queryset=Compound.objects.all(), empty_label='اختر المجمع', widget=forms.Select(attrs={'class':'dropdown'}))
    @property
    
    def helper(self):
        helper= FormHelper()
        helper.layout=Layout(
            HTML(' <h1 class="text-center text-info">البحث فى  الوحدات</h1>'),
        )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'بحث ', css_class='btn btn-info'))
        helper.field_class="col-lg-9 col-sm-12"
        helper.label_class="col-3"
        return helper
