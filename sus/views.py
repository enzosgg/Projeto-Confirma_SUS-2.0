from django.shortcuts import render, redirect, get_object_or_404
from core.models import Paciente, Consulta, Medico
from core.decorators import login_required_paciente

@login_required_paciente
def plataforma(request):
    paciente = get_object_or_404(Paciente, id=request.session['paciente_id'])
    consultas = Consulta.objects.filter(
        paciente=paciente
    ).exclude(status='compareceu').exclude(status='naocompareceu').order_by('data', 'hora')
    
    return render(request, 'plataforma.html', {'paciente': paciente,'consultas': consultas})

@login_required_paciente
def marcar_consulta(request):
    paciente = get_object_or_404(Paciente, id=request.session['paciente_id'])
    especialidade = request.GET.get('especialidade')

    consultas_disponiveis = Consulta.objects.filter(paciente__isnull=True).order_by('data', 'hora')
    
    if especialidade:
        consultas_disponiveis = consultas_disponiveis.filter(medico__especialidade=especialidade)
    
    especialidades = Medico.objects.values_list('especialidade', flat=True).distinct()
    
    return render(request, 'marcar_consulta.html', {'paciente': paciente,'consultas_disponiveis': consultas_disponiveis,'especialidades': especialidades,'especialidade_selecionada': especialidade})

@login_required_paciente
def confirmar_marcacao(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    consulta.paciente_id = request.session['paciente_id']
    consulta.status = 'agendada'
    consulta.save()
    return redirect('plataforma')

@login_required_paciente
def perfil(request):
    paciente = get_object_or_404(Paciente, id=request.session['paciente_id'])

    if request.method == 'POST':
        paciente.telefone = request.POST.get('telefone')
        paciente.email = request.POST.get('email')
        paciente.save()
        return redirect('plataforma')
    
    return render(request, 'perfil.html', {'paciente': paciente})

@login_required_paciente
def consulta(request, id):
    consulta = get_object_or_404(Consulta.objects.select_related('medico', 'paciente'), id=id,paciente_id=request.session['paciente_id'])

    return render(request, 'consulta.html', {'consulta': consulta})

@login_required_paciente
def confirmar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id, paciente_id=request.session['paciente_id'])
    consulta.status = 'confirmada'
    consulta.save()
    return redirect('plataforma')

@login_required_paciente
def cancelar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id, paciente_id=request.session['paciente_id'])
    consulta.paciente = None
    consulta.status = 'aguardando'
    consulta.save()
    
    return redirect('plataforma')

@login_required_paciente
def reagendar(request, id):
    consulta_atual = get_object_or_404(Consulta.objects.select_related('medico'), id=id,paciente_id=request.session['paciente_id'])
    consultas_reagendamento = Consulta.objects.filter(paciente__isnull=True,medico__especialidade=consulta_atual.medico.especialidade).order_by('data', 'hora')

    return render(request, 'reagendar.html', {'consulta_atual': consulta_atual,'consultas_reagendamento': consultas_reagendamento})

@login_required_paciente
def confirmar_reagendamento(request, consulta_atual_id, nova_consulta_id):
    paciente = get_object_or_404(Paciente, id=request.session['paciente_id'])
    consulta_atual = get_object_or_404(Consulta, id=consulta_atual_id, paciente=paciente)
    nova_consulta = get_object_or_404(Consulta, id=nova_consulta_id, paciente__isnull=True)
    consulta_atual.paciente = None
    consulta_atual.status = 'aguardando'
    consulta_atual.save()
    nova_consulta.paciente = paciente
    nova_consulta.status = 'agendada'
    nova_consulta.save()

    return redirect('plataforma')

def logout(request):
    if 'paciente_id' in request.session:
        del request.session['paciente_id']
    return redirect('recepcao')