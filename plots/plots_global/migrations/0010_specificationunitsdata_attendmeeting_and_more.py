# Generated by Django 4.0.3 on 2022-03-22 18:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('plots_global', '0009_remove_specificationunitsdata_services_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specificationunitsdata',
            name='AttendMeeting',
            field=models.BooleanField(default=False, help_text='هل حضر اجتماعات الهيئة  ', verbose_name=' هل حضر اجتماعات الهيئة '),
        ),
        migrations.AddField(
            model_name='specificationunitsdata',
            name='ContactNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='التليفون و الفاكسات', max_length=128, null=True, region=None, verbose_name='التليفون'),
        ),
    ]
