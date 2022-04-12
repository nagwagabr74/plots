from django import forms

from .models import SpecificationUnitsData,Governerates, Compound




class Chart_unitStatusFormModel(forms.ModelForm):
    class Meta:
       
        model = Compound
        
        
        fields = ["CompoundName"]

   
    
    CompoundName= forms.ModelChoiceField(label='اختر المجمع ',required=False, queryset=Compound.objects.all(), empty_label='اختر المجمع', widget=forms.Select(attrs={'class':'dropdown'}))
    