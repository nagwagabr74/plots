# Generated by Django 4.0.3 on 2022-03-22 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plots_global', '0014_alter_specificationunitsdata_subactivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specificationunitsdata',
            name='UnitProblemsSolutions',
            field=models.TextField(blank=True, max_length=1500, null=True, verbose_name='  الاجراءات بخصوص تلك المشكلات'),
        ),
    ]