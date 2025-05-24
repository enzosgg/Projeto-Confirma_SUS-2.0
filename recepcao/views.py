from django.shortcuts import render,redirect 
from core.models import Paciente, Medico

def recepcao(request):
    return render (request,'recepcao.html')

def login_paciente(request):
    if request.method == "GET":
        status = request.GET.get('status')
        return render(request, 'login_paciente.html', {'status': status})
    elif request.method == "POST":
        cpf = request.POST.get('cpf_sem_formatacao')
        senha = request.POST.get('senha')
        paciente = Paciente.objects.filter(cpf=cpf, senha=senha).first()

        if paciente:
            request.session['paciente_id'] = paciente.id
            return redirect('plataforma')
        else:
            return redirect('/login_paciente/?status=1')
        
def login_medico(request):
    if request.method == "GET":
        status = request.GET.get('status')
        return render(request, 'login_medico.html', {'status': status})
    elif request.method == "POST":
        crm = request.POST.get('crm')
        senha = request.POST.get('senha')
        medico = Medico.objects.filter(crm=crm, senha=senha).first()

        if medico:
            request.session['medico_id'] = medico.id
            return redirect('plataforma_medico')
        else:
            return redirect('/login_medico/?status=1')
        
def senha(request):
    if request.method == "GET":
        status = request.GET.get('status')
        return render(request, 'senha.html', {'status': status})
    elif request.method == "POST":
        cpf = request.POST.get('cpf_sem_formatacao')
        paciente = Paciente.objects.filter(cpf=cpf).first()

        if paciente:
            return redirect('/senha/?status=2')
        else:
            return redirect('/senha/?status=1')
