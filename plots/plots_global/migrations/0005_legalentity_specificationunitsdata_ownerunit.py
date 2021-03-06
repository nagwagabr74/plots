# Generated by Django 4.0.3 on 2022-03-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plots_global', '0004_alter_specificationunitsdata_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LegalEntityName', models.CharField(help_text='الكيان القانونى', max_length=70, unique=True, verbose_name='الكيان القانونى')),
            ],
            options={
                'verbose_name': 'الكيان القانونى',
                'verbose_name_plural': 'الكيانات القانونية',
                'ordering': ['LegalEntityName'],
            },
        ),
        migrations.AddField(
            model_name='specificationunitsdata',
            name='OwnerUnit',
            field=models.CharField(default=1, max_length=150, verbose_name='اسم المالك'),
            preserve_default=False,
        ),
    ]
