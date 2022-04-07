from django.contrib import admin
from .models import Governerates, Compound, Activities, SpecificationUnitsData, LegalEntity, LandOperatingStatus
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User




# Register your models here.
@admin.register(Governerates)
class GoverneratesAdmin(ImportExportModelAdmin):
    search_fields = ['Governerate__GovernerateName__icontains']
    pass

@admin.register(LandOperatingStatus)
class LandOperatingStatusAdmin(ImportExportModelAdmin):
    search_fields = ['LandOperatingStatus__LandOperatingStatusName__icontains']
    pass
@admin.register(LegalEntity)
class LegalEntityAdmin(ImportExportModelAdmin):
    search_fields = ['LegalEntity__LegalEntityName__icontains']
    pass

@admin.register(Compound)
class CompoundAdmin(ImportExportModelAdmin):
    list_per_page = 11
    search_fields = ['Compound__CompoundName__icontains']
    pass
    
@admin.register(Activities)
class ActivitiesAdmin(ImportExportModelAdmin):
    list_per_page = 11
    pass


@admin.register(SpecificationUnitsData)
class SpecificationUnitsDataAdmin(ImportExportModelAdmin):
    list_per_page = 50
    search_fields = ['OwnerUnit__icontains','GoverneratesId__GovernerateName__icontains','UnitNumber__icontains','CompoundId__CompoundName__icontains']    
    list_display = ('UnitNumber','CompoundId','GoverneratesId','OwnerUnit','LandOperatingStatus','HandedDate','SubActivity',) 
    list_filter=('Main_Activity','LandOperatingStatus','LegalEntity','CompoundId')
    # readonly_fields = ('GoverneratesId','CompoundId','UnitNumber','OwnerUnit','LegalEntity')
    
  
    fields = []  
    def change_view(self, request, object_id, extra_context=None):  # override default admin change behaviour
        
        main=['GoverneratesId','CompoundId','UnitNumber','OwnerUnit','LegalEntity','ContactNumber']
        
        if request.user.groups.filter(name="units").exists():  
            AppendFields=['UnitsCount','UnitArea','TotalArea','Main_Activity','LandOperatingStatus','SpecificationDate','HandedDate','CommitteeNumber']
   
        elif request.user.groups.filter(name="idc").exists():  
            AppendFields=['LandOperatingStatus','SubActivity','Has_Electric_Meter','Has_Water_Meter','Has_equipment','UnitProblems','UnitProblemsSolutions','UnitNotWorkReasons','UnitNotes']
            
        elif request.user.groups.filter(name="eng_service").exists(): 
            AppendFields=['OperatingLicense','industrialRegistry']
           

        elif request.user.groups.filter(name="finance").exists():  
            AppendFields=['DuePriceOrrent','DueServices','Has_Finance']
        else :
            AppendFields=main
             
   
        for field in AppendFields :
                if field not in main:
                     main.append(field)
        self.fields=main
        return super(SpecificationUnitsDataAdmin, self).change_view(request,object_id )







