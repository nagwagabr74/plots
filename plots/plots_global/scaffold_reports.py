# from bar import app
from .models import SpecificationUnitsData
from scaffold_report.report import ScaffoldReport, scaffold_reports

class SpecificationUnitsDataReport(ScaffoldReport):
    name = "Reports"
    model = SpecificationUnitsData
    filters = (
    )

scaffold_reports.register('SpecificationUnitsData_report', SpecificationUnitsDataReport)