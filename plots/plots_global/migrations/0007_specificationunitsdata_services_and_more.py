# Generated by Django 4.0.3 on 2022-03-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plots_global', '0006_landoperatingstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specificationunitsdata',
            name='Services',
            field=models.FloatField(blank=True, null=True, verbose_name='الخدمات'),
        ),
        migrations.AddField(
            model_name='specificationunitsdata',
            name='rent',
            field=models.FloatField(blank=True, null=True, verbose_name='الخدمات'),
        ),
    ]
