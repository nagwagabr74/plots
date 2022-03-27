# Generated by Django 4.0.3 on 2022-03-22 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plots_global', '0007_specificationunitsdata_services_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specificationunitsdata',
            name='LegalEntity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plots_global.legalentity', verbose_name='كود الكيان القانونى'),
        ),
        migrations.AlterField(
            model_name='specificationunitsdata',
            name='UnitModification',
            field=models.TextField(max_length=1000, verbose_name='التعديلات على الوحدة'),
        ),
        migrations.AlterField(
            model_name='specificationunitsdata',
            name='UnitNotWorkReasons',
            field=models.TextField(max_length=1500, verbose_name='  اسباب عدم العمل حتى الان'),
        ),
        migrations.AlterField(
            model_name='specificationunitsdata',
            name='UnitNotes',
            field=models.TextField(max_length=1500, verbose_name='  ملاحظات'),
        ),
        migrations.AlterField(
            model_name='specificationunitsdata',
            name='UnitProblems',
            field=models.TextField(max_length=1500, verbose_name=' المشاكل التى تواجهة المستثمر '),
        ),
        migrations.AlterField(
            model_name='specificationunitsdata',
            name='UnitProblemsSolutions',
            field=models.TextField(max_length=1500, verbose_name='  الاجراءات بخصوص تلك المشكلات'),
        ),
    ]
