# Generated by Django 5.1.6 on 2025-04-02 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_consulta_data_conclusao_alter_consulta_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='data_atualizacao',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='data_conclusao',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='estatisticas',
            name='consultas_canceladas',
        ),
        migrations.RemoveField(
            model_name='estatisticas',
            name='consultas_concluidas',
        ),
        migrations.RemoveField(
            model_name='estatisticas',
            name='consultas_confirmadas',
        ),
        migrations.RemoveField(
            model_name='estatisticas',
            name='data_registro',
        ),
        migrations.AddField(
            model_name='estatisticas',
            name='consultas_comparecidas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='estatisticas',
            name='consultas_nao_comparecidas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='status',
            field=models.CharField(choices=[('aguardando', 'Aguardando'), ('agendada', 'Agendada'), ('confirmada', 'Na unidade'), ('compareceu', 'Compareceu'), ('naocompareceu', 'Não compareceu')], default='agendada', max_length=20),
        ),
    ]
