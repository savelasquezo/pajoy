# Generated by Django 4.2.1 on 2023-05-23 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='date',
            field=models.TimeField(default=datetime.date.today, help_text='Fecha de Inicio del Tour', verbose_name='Fecha:'),
        ),
    ]
