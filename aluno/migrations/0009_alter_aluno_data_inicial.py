# Generated by Django 5.2.1 on 2025-06-11 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0008_alter_aluno_data_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_inicial',
            field=models.DateField(default=datetime.datetime(2025, 6, 11, 23, 45, 39, 17619, tzinfo=datetime.timezone.utc), help_text='Informe a data inicial de matrícula do Aluno'),
        ),
    ]
