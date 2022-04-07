from django import forms

from .models import SpecificationUnitsData,Governerates




class Chart_unitStatusFormModel(forms.ModelForm):
    class Meta:
        # fields = ('name', 'title', 'birth_date')
        # labels = {
        #     'name': _('Writer'),
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }
        # field_classes = {
        #     'slug': MySlugFormField,
        # }
        
        # widgets={'name': Textarea(attrs={'cols': 80, 'rows': 20})})
        # localized_fields=('birth_date',))
        model = Governerates
        
        
        fields = ["GovernerateName"]

   
    
    GovernerateName= forms.ModelChoiceField(label='اختر نوع الخبر',required=False, queryset=Governerates.objects.all(), empty_label='اختر نوع الخبر', widget=forms.Select(attrs={'class':'dropdown'}))
    