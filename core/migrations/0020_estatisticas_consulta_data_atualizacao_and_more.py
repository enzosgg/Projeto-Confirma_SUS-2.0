# Generated by Django 5.1.6 on 2025-04-01 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_consulta_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estatisticas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registro', models.DateTimeField(auto_now_add=True, null=True)),
                ('consultas_totais', models.PositiveIntegerField(default=0)),
                ('consultas_agendadas', models.PositiveIntegerField(default=0)),
                ('consultas_confirmadas', models.PositiveIntegerField(default=0)),
                ('consultas_concluidas', models.PositiveIntegerField(default=0)),
                ('consultas_canceladas', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='consulta',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='ConsultaHistorico',
        ),
    ]
