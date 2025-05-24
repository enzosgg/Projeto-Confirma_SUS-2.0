from django.shortcuts import render, redirect, get_object_or_404
from core.models import Medico, Consulta
from core.decorators import login_required_medico

@login_required_medico
def plataforma_medico(request):
    medico = get_object_or_404(Medico, id=request.session['medico_id'])
    consultas = Consulta.objects.filter(medico=medico,paciente__isnull=False
    ).exclude(status='compareceu').exclude(status='naocompareceu').order_by('-data', 'hora')
    
    return render(request, 'plataforma_medico.html', {'medico': medico,'consultas': consultas})

@login_required_medico    
def consulta_medico(request, id):
    consulta = get_object_or_404(Consulta.objects.select_related('medico', 'paciente'), id=id)
    return render(request, 'consulta_medico.html', {'consulta': consulta})

@login_required_medico
def paciente_compareceu(request, id):
    consulta = get_object_or_404(Consulta, id=id, medico_id=request.session['medico_id'])

    consulta.status = 'compareceu'
    consulta.save()
    
    return redirect('plataforma_medico')

@login_required_medico
def paciente_nao_compareceu(request, id):
    consulta = get_object_or_404(Consulta, id=id, medico_id=request.session['medico_id'])

    consulta.status = 'naocompareceu'
    consulta.save()
    
    return redirect('plataforma_medico')

def logout_medico(request):
    if 'medico_id' in request.session:
        del request.session['medico_id']
    return redirect('recepcao')