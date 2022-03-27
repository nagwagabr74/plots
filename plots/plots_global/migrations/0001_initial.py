# Generated by Django 4.0.3 on 2022-03-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Governerates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GovernerateName', models.CharField(help_text='اسم المحافظة يجب ان يكون غير مدرج من قبل', max_length=20, unique=True, verbose_name='المحافظه')),
            ],
            options={
                'verbose_name': 'المحافظه',
                'verbose_name_plural': 'المحافظات',
                'ordering': ['GovernerateName'],
            },
        ),
    ]