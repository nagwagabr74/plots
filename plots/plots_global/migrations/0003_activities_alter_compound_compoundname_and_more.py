# Generated by Django 4.0.3 on 2022-03-22 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plots_global', '0002_compound'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActivityName', models.CharField(help_text='نشاط صناعي رئيسي', max_length=40, unique=True, verbose_name='النشاط')),
            ],
            options={
                'verbose_name': 'النشاط',
                'verbose_name_plural': 'الانشطه',
                'ordering': ['ActivityName'],
            },
        ),
        migrations.AlterField(
            model_name='compound',
            name='CompoundName',
            field=models.CharField(help_text='اسم المجمع يجب ان يكون غير مدرج من قبل', max_length=20, unique=True, verbose_name='المجمع'),
        ),
        migrations.CreateModel(
            name='SpecificationUnitsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UnitsCount', models.PositiveIntegerField(default=0, verbose_name='عدد الوحدات ')),
                ('UnitArea', models.PositiveIntegerField(default=0, help_text=' مساحة الوحدة  ', verbose_name=' مساحة الوحدة')),
                ('TotalArea', models.PositiveIntegerField(default=0, help_text=' إجمالي المساحة المخصصة', verbose_name=' إجمالي المساحة المخصصة')),
                ('CompoundId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plots_global.compound', verbose_name='كود المجمع')),
                ('GoverneratesId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plots_global.governerates', verbose_name='كود المحافظة')),
                ('Main_Activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='plots_global.activities', verbose_name='كود القطاع الصناعى')),
            ],
            options={
                'verbose_name': 'بيانات الوحدة المخصصة',
                'verbose_name_plural': 'بيانات الوحدة المخصصة',
            },
        ),
    ]
