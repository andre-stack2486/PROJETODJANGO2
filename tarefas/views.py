from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefas
from .forms import TarefaForm
from django.contrib.auth.decorators import  login_required

# Create your views here.
@login_required
def listaTarefa(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at')
    return render(request, 'tarefas/list.html', {'tarefas': tarefas_list})

@login_required
def novaTarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        form.save()
        return redirect('/')
    
    else:
        form = TarefaForm()
        return render(request, 'tarefas/addTarefa.html', {'form':form})

@login_required   
def tarefaView(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render (request, 'tarefas/tarefa.html', {'tarefa':tarefa})


@login_required
def editTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    form = TarefaForm(instance=tarefa)

    if(request.method == 'POST'):
        form = TarefaForm(request.POST, instance=tarefa)

        if(form.is_valid()):
            tarefa.save()
            return redirect('/')
        else:
            return render(request, 'tarefas/editTarefa.html', {'form':form, 'tarefa':tarefa})
        
    else:
        return render(request, 'tarefas/editTarefa.html', {'form':form, 'tarefa':tarefa})

@login_required
def deleteTarefa(request, id):
     tarefa = get_object_or_404(Tarefas, pk=id)
     tarefa.delete()
     return redirect('/')