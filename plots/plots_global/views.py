from django.shortcuts import render
from .models import SpecificationUnitsData, Compound
from plots_global import models as plots_global
from django.db.models import Count, F, Sum, Avg
from django.http import JsonResponse
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
from django.http import HttpResponse
from django.views.generic import View
from .filters import UnitsDataFilter
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit
from .forms import Chart_unitStatusFormModel
from django.db.models import Q

# from weasyprint import HTML
# Create your views here.

class UnitListView(FilterView,ExportMixin,SingleTableView,ListView):
    model=SpecificationUnitsData
    filterset_class = UnitsDataFilter
    template_name="plots_global/unitdata_list.html"
    #queryset=SpecificationUnitsData.objects.all()
    context_object_name='unitsdata'
    
    count = SpecificationUnitsData.objects.count()
    paginate_by = 70
  
    
    
class UnitsDataFilter(FilterView,ExportMixin,SingleTableView):
        model =SpecificationUnitsData
        filterset_class = UnitsDataFilter
        template_name="plots_global/SpecificationUnitsData_filter.html"
        # queryset=SpecificationUnitsData.objects.all().order_by('-pk')
    
 
def html_to_pdf_view(request):
    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    html_string = render_to_string('core/pdf_template.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response


def chart_operations(request):
    working1_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='استيفاء اقتصادى').count()
    working2_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='استيفاء مالى').count()
    working3_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='استيفاء مستندات').count()
    working4_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='تحت التجهيز').count()
    working5_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='تشغيل متقطع').count()
    working6_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='جارى الاستلام').count()
    working7_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='جارى السحب').count()
    working8_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='لا يعمل').count()
    working9_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='لم يتم الاستلام').count()
    working10_count =SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='مخزن').count()
    working11_count =SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='مغلق').count()
    working12_count =SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='يعمل').count()
    working13_count =SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='شاغرة').count()



    
    return render(request, 'plots_global/chart_operations.html',{
        
        'working1_count': working1_count ,
        'working2_count': working2_count ,
        'working3_count': working3_count ,
        'working4_count': working4_count ,
        'working5_count': working5_count ,
        'working6_count': working6_count ,
        'working7_count': working7_count ,
        'working8_count': working8_count ,
        'working9_count': working9_count ,
        'working10_count': working10_count ,
        'working11_count': working11_count ,
        'working12_count': working12_count ,
        'working13_count': working13_count ,


    })
    
    #########################################
def chart_activities(request):
    activities1_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='تعدين').count()
    activities2_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='جلود').count()
    activities3_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='دوائى').count()
    activities4_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='غذائي').count()
    activities5_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='غزل ونسيج').count()
    activities6_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='قوى').count()
    activities7_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='كيماوى').count()
    activities8_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='معدنى').count()
    activities9_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='هندسي').count()


    
    return render(request, 'plots_global/chart_activities.html',{
    
        'activities1_count': activities1_count ,
        'activities2_count': activities2_count ,
        'activities3_count': activities3_count ,
        'activities4_count': activities4_count ,
        'activities5_count': activities5_count ,
        'activities6_count': activities6_count ,
        'activities7_count': activities7_count ,
        'activities8_count': activities8_count ,
        'activities9_count': activities9_count 
        

    })
    
from plots_global.utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        unitsdata = SpecificationUnitsData.objects.all()
        data = {    
            'unitsdata':unitsdata,
            'request': request
        }
        pdf = render_to_pdf('plots_global/unitdata_list.html',data)
        return HttpResponse(pdf, content_type='application/pdf')

class chart_activitiesPdf(View):
    def get(self, request, *args, **kwargs):
        activities1_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='تعدين').count()
        activities2_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='جلود').count()
        activities3_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='دوائى').count()
        activities4_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='غذائي').count()
        activities5_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='غزل ونسيج').count()
        activities6_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='قوى').count()
        activities7_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='كيماوى').count()
        activities8_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='معدنى').count()
        activities9_count = SpecificationUnitsData.objects.filter(Main_Activity__ActivityName='هندسي').count()
        data = {    
            'activities1_count': activities1_count ,
            'activities2_count': activities2_count ,
            'activities3_count': activities3_count ,
            'activities4_count': activities4_count ,
            'activities5_count': activities5_count ,
            'activities6_count': activities6_count ,
            'activities7_count': activities7_count ,
            'activities8_count': activities8_count ,
            'activities9_count': activities9_count ,
            'request': request
        }
        pdf = render_to_pdf('plots_global/chart_activities.html',data)
        return HttpResponse(pdf, content_type='application/pdf')
    
class chart_operationsPdf(View):
    def get(self, request, *args, **kwargs):
            working1_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='استيفاء اقتصادى').count()
            working2_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='استيفاء مالى').count()
            working3_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='استيفاء مستندات').count()
            working4_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='تحت التجهيز').count()
            working5_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='تشغيل متقطع').count()
            working6_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='جارى الاستلام').count()
            working7_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='جارى السحب').count()
            working8_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='لا يعمل').count()
            working9_count = SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='لم يتم الاستلام').count()
            working10_count =SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='مخزن').count()
            working11_count =SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='مغلق').count()
            working12_count =SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='يعمل').count()

            data = {    
                'working1_count': working1_count ,
                'working2_count': working2_count ,
                'working3_count': working3_count ,
                'working4_count': working4_count ,
                'working5_count': working5_count ,
                'working6_count': working6_count ,
                'working7_count': working7_count ,
                'working8_count': working8_count ,
                'working9_count': working9_count ,
                'working10_count': working10_count ,
                'working11_count': working11_count ,
                'working12_count': working12_count ,
                'request': request
            }
            pdf = render_to_pdf('plots_global/unitdata_list.html',data)
            return HttpResponse(pdf, content_type='application/pdf')    
        
        
from wkhtmltopdf.views import PDFTemplateView


class MyPDF(PDFTemplateView):
    def get(self, request, *args, **kwargs):
        unitsdata = SpecificationUnitsData.objects.all()
        data = {    
                'unitsdata': unitsdata ,
                'request': request
            }
    filename = 'my_pdf.pdf'
    template_name = 'plots_global/unitdata_list2.html'

    options = {
            'page-size': 'A3',
            'encoding': "UTF-8",
        }
##############################################################


class Chart_unitStatus(View):
    form_class = Chart_unitStatusFormModel
    initial = {'key': 'value'}
    template_name = 'plots_global/chart_UnitStatus.html'

    def get(self, request, *args, **kwargs):
        
        if request.GET.get('CompoundName'):
            form = self.form_class(initial={'CompoundName':request.GET.get('CompoundName')})
            working1_count =SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='شاغرة',CompoundId=request.GET.get('CompoundName')).count()
            working2_count =SpecificationUnitsData.objects.filter(~Q(LandOperatingStatus__LandOperatingStatusName='شاغرة'),CompoundId=request.GET.get('CompoundName')).count()
        else:
            form = self.form_class(initial=self.initial)
            working1_count =SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='شاغرة').count()
            working2_count =SpecificationUnitsData.objects.filter(~Q(LandOperatingStatus__LandOperatingStatusName='شاغرة')).count()
        return render(request, self.template_name, {'form': form, 'working1_count': working1_count ,
        'working2_count': working2_count })

    

class chart_unitStatusPdf(View):
    def get(self, request, *args, **kwargs):
        working1_count =SpecificationUnitsData.objects.filter(LandOperatingStatus__LandOperatingStatusName='شاغرة').count()
        working2_count =SpecificationUnitsData.objects.filter(~Q(LandOperatingStatus__LandOperatingStatusName='شاغرة')).count()

        data = {    
                'emptyunits1_count': emptyunits1_count ,
                'emptyunits2_count': emptyunits2_count ,
                'request': request
            }
        pdf = render_to_pdf('plots_global/chart_UnitStatus.html',data)
        return HttpResponse(pdf, content_type='application/pdf')   


########################
colorPalette = ['#55efc4', '#81ecec', '#a29bfe', '#ffeaa7', '#fab1a0', '#ff7675', '#fd79a8']
colorPrimary, colorSuccess, colorDanger = '#79aec8', colorPalette[0], colorPalette[5]
def generate_color_palette(amount):
    palette = []

    i = 0
    while i < len(colorPalette) and len(palette) < amount:
        palette.append(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < amount:
            i = 0

    return palette


# @staff_member_required
def stacked_chart(request):
    # units = SpecificationUnitsData.objects.filter(CompoundId__CompoundName=cname)
    grouped_units = SpecificationUnitsData.objects.all().values('CompoundId').annotate(count=Count('pk'))\
        .values('CompoundId', 'count').order_by('CompoundId')

    cname_dict = dict()

    for compound in Compound.objects.all().values_list('CompoundName',flat=True):
        cname_dict[str(compound)] = 0

    # for group in grouped_units:
    #     cname_dict[dict(Compound.objects.all())[group['CompoundId']]] = group['count']

    return JsonResponse({
       'title': 'عدد الوحدات بكل مجمع ',
        'data': {
            'labels': list(cname_dict.keys()),
            'datasets': [{
                'label': 'Count',
                'backgroundColor': generate_color_palette(len(cname_dict)),
                'borderColor': generate_color_palette(len(cname_dict)),
                'data': list(grouped_units.values_list('count',flat=True)),
            }]
        },
    })


# @staff_member_required
def statistics_view(request):
    return render(request, 'plots_global/chart_stacked.html', {})


class chart_stackedcomponds(View):
    def get(self, request, *args, **kwargs):
            componds1_count = SpecificationUnitsData.objects.filter(CompoundId__CompoundName='السادات').count()
            componds2_count = SpecificationUnitsData.objects.filter(CompoundId__CompoundName='الغردقة').count()
            componds3_count = SpecificationUnitsData.objects.filter(CompoundId__CompoundName='المحلة').count()
            componds4_count = SpecificationUnitsData.objects.filter(CompoundId__CompoundName='المنيا').count()
            componds5_count = SpecificationUnitsData.objects.filter(CompoundId__CompoundName='بورسعيد').count()
            componds6_count = SpecificationUnitsData.objects.filter(CompoundId__CompoundName='سوهاج').count()
            componds7_count = SpecificationUnitsData.objects.filter(CompoundId__CompoundName='مجمع الأقصر').count()
            v8_count = SpecificationUnitsData.objects.filter(CompoundId__CompoundName='مرغم').count()

            data = {    
                'componds1_count': componds1_count ,
                'componds2_count': componds2_count ,
                'componds3_count': componds3_count ,
                'componds4_count': componds4_count ,
                'componds5_count': componds5_count ,
                'componds6_count': componds6_count ,
                'componds7_count': componds7_count ,
                'componds8_count': componds8_count ,
                'request': request
            }
            pdf = render_to_pdf('plots_global/chart_stacked.html',data)
            return HttpResponse(pdf, content_type='application/pdf')    
        
        
