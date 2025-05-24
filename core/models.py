from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    senha = models.CharField(max_length=128, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=128, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nome 
    
class Medico(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    crm = models.CharField(max_length=11, unique=True, null=True, blank=True)
    senha = models.CharField(max_length=128, null=True, blank=True)
    especialidade = models.CharField(max_length=128, null=True, blank=True)
    consultorio = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    status_escolhas = [('aguardando', 'Aguardando'),('agendada', 'Agendada'),('confirmada', 'Na unidade'),('compareceu', 'Compareceu'),('naocompareceu', 'Não compareceu')]
    status_retorno = [('retorno', 'Paciente retornando'), ('primeira_consulta', 'Primeira consulta do paciente')]

    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, blank=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=status_escolhas, default='agendada')
    retorno_ou_primeira_consulta = models.CharField(max_length=20, choices=status_retorno, default='primeira_consulta')

    def __str__(self):
        return f"{self.medico.nome} - {self.data} {self.hora} ({self.status})"

class Estatisticas(models.Model):
    consultas_totais = models.PositiveIntegerField(default=0)
    consultas_agendadas = models.PositiveIntegerField(default=0)
    consultas_comparecidas = models.PositiveIntegerField(default=0)
    consultas_nao_comparecidas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Estatísticas em {self.data_registro.strftime('%d/%m/%Y %H:%M')}"