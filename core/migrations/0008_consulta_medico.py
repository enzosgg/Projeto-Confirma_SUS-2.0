# Generated by Django 5.1.6 on 2025-03-12 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_consulta_especialidade_remove_consulta_medico'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='core.medico'),
        ),
    ]
