# Generated by Django 4.0.3 on 2022-03-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plots_global', '0020_alter_specificationunitsdata_legalentity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specificationunitsdata',
            name='OperatingLicense',
            field=models.BooleanField(blank=True, default=False, help_text='هل يوجد رخصة تشغيل  ', null=True, verbose_name='رخصة تشغيل'),
        ),
        migrations.AlterField(
            model_name='specificationunitsdata',
            name='industrialRegistry',
            field=models.BooleanField(blank=True, default=False, help_text='هل يوجد سجل صناعى  ', null=True, verbose_name=' سجل صناعى'),
        ),
    ]
