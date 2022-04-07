
from django.urls import path
from django.conf.urls import url, include
from . import views
from .views import GeneratePdf
from wkhtmltopdf.views import PDFTemplateView
from django_pdfkit import PDFView


urlpatterns = [

    # path('', views.home, name='home'),
    path('', views.UnitListView.as_view(), name='UnitsData'),
    path('search', views.UnitsDataFilter.as_view(), name='search'),
    path('operations', views.chart_operations, name='chart_operations'),
    path('activities', views.chart_activities, name='chart_activities'),
    path('unitStatus', views.Chart_unitStatus.as_view(), name='chart_unitStatus'),

    path('doc', views.GeneratePdf.as_view(), name='pdf'),
    path('activitiesPdf', views.chart_activitiesPdf.as_view(), name='chart_activitiesPdf'),
    path('operationsPdf', views.chart_operationsPdf.as_view(), name='chart_operationsPdf'),

    path('unitStatusPdf', views.chart_operationsPdf.as_view(), name='chart_unitStatusPdf'),


    path('ss', PDFTemplateView.as_view(template_name='plots_global/unitdata_list2.html',
                                           filename='my_pdf.pdf'), name='pdf1'),
    path('my-pdf', PDFView.as_view(template_name='plots_global/unitdata_list2.html'), name='my-pdf'),



    

    
]