

import csv
import re

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from plots_global.models import SpecificationUnitsData


#python manage.py loadcsv --csv plots_global/management/commands/proj.csv


class Command(BaseCommand):
    help = 'Load the reviews data from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('--csv', type=str)

    @staticmethod
    def row_to_dict(row, header):
        if len(row) < len(header):
            row += [''] * (len(header) - len(row))
        return dict([(header[i], row[i]) for i, head in enumerate(header) if head])

    def handle(self, *args, **options):
        m = re.compile(r'content:(\w+)')
        header = None
        models = dict()
        try:
            with open(options['csv']) as csvfile:
                model_data = csv.reader(csvfile)
                for i, row in enumerate(model_data):
                    if max([len(cell.strip()) for cell in row[1:] + ['']]) == 0 and m.match(row[0]):
                        model_name = m.match(row[0]).groups()[0]
                        models[model_name] = []
                        header = None
                        continue

                    if header is None:
                        header = row
                        continue

                    row_dict = self.row_to_dict(row, header)
                    if set(row_dict.values()) == {''}:
                        continue
                    models[model_name].append(row_dict)

        except FileNotFoundError:
            raise CommandError('File "{}" does not exist'.format(options['csv']))

        for data_dict in models.get('SpecificationUnitsData', []):
            p, created = SpecificationUnitsData.objects.get_or_create(GoverneratesId=data_dict['GoverneratesId'], defaults={
                'CompoundId': data_dict['CompoundId'],
                'UnitNumber': data_dict['UnitNumber'],
                'UnitsCount': data_dict['UnitsCount'],
                'UnitArea': data_dict['UnitArea'],
                'TotalArea': data_dict['TotalArea'],
                'Main_Activity': data_dict['Main_Activity'],
                'RequestNumber': data_dict['RequestNumber'],
                'OwnerUnit': data_dict['OwnerUnit'],
                'LegalEntity': data_dict['LegalEntity'],
                'CommitteeNumber': data_dict['CommitteeNumber'],
                'SpecificationDate': data_dict['SpecificationDate'],
                'HandedDate': data_dict['HandedDate'],
                'LandOperatingStatus': data_dict['LandOperatingStatus'],
                'SubActivity': data_dict['SubActivity'],
                'OperatingLicense': data_dict['OperatingLicense'],
                'industrialRegistry': data_dict['industrialRegistry'],
                'DeclarationModification': data_dict['DeclarationModification'],
                'UnitModification': data_dict['UnitModification'],
                'Has_Electric_Meter': data_dict['Has_Electric_Meter'],
                'Has_Water_Meter': data_dict['Has_Water_Meter'],
                'Has_equipment': data_dict['Has_equipment'],
                'DueServices': data_dict['DueServices'],
                'DuePriceOrrent': data_dict['DuePriceOrrent'],
                'Has_Finance': data_dict['Has_Finance'],
                'UnitProblems': data_dict['UnitProblems'],
                'UnitProblemsSolutions': data_dict['UnitProblemsSolutions'],
                'UnitNotWorkReasons': data_dict['UnitNotWorkReasons'],
                'AttendMeeting': data_dict['AttendMeeting'],
                'UnitNotes': data_dict['UnitNotes']



            })

            if created:
                print('Created SpecificationUnitsData "{}"'.format(p.name))

        print("Import complete")
