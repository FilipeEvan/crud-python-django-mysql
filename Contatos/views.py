from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import *
from django.contrib import messages

from .models import *

# Create your views here.

# Contatos
def listarContatos(request):
    busca = request.GET.get('consulta')

    if busca:
        contatos = Contato.objects.filter(nome__icontains=busca)
    else:
        lista_contatos = Contato.objects.all().order_by('nome')
        # lista_contatos = Contato.objects.all().order_by('-create_data')

        paginator = Paginator(lista_contatos, 5)

        page = request.GET.get('page')

        contatos = paginator.get_page(page)

    return render(request, 'contatos/list.html', {'contatos': contatos})

def verContato(request, id):
    contato = get_object_or_404(Contato, pk=id)
    return render(request, 'contatos/retrieve.html', {'contato': contato})

def criarContato(request):
    if request.method == 'POST':
        form = formularioContato(request.POST)

        if form.is_valid():
            contato = form.save(commit=False)
            contato.save()

            messages.success(request, 'Contato criado com sucesso.')

            return redirect('/')

    else:
        form = formularioContato()
        return render(request, 'contatos/create.html', {'form': form})

def editarContato(request, id):
    contato = get_object_or_404(Contato, pk=id)
    form = formularioContato(instance=contato)

    if request.method == 'POST':
        form = formularioContato(request.POST, instance=contato)

        if form.is_valid():
            contato.save()

            messages.success(request, 'Contato atualizado com sucesso.')

            return redirect('/')
        else:
            return render(request, 'contatos/edit.html', {'form': form, 'contato': contato})

    else:
        return render(request, 'contatos/edit.html', {'form': form, 'contato': contato})

def deletarContato(request, id):
    contato = get_object_or_404(Contato, pk=id)
    contato.delete()

    messages.info(request, 'Contato deletado com sucesso.')

    return redirect('/')

# Grupos
def listarGrupos(request):
    busca = request.GET.get('consulta')

    if busca:
        grupos = Grupo.objects.filter(titulo__icontains=busca)
    else:
        lista_grupos = Grupo.objects.all().order_by('-create_data')

        paginator = Paginator(lista_grupos, 3)

        page = request.GET.get('page')

        grupos = paginator.get_page(page)

    return render(request, 'grupos/list.html', {'grupos': grupos})

def verGrupo(request, id):
    grupo = get_object_or_404(Grupo, pk=id)
    return render(request, 'grupos/retrieve.html', {'grupo': grupo})

def criarGrupo(request):
    if request.method == 'POST':
        form = formularioGrupo(request.POST)

        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.save()

            messages.success(request, 'Grupo criado com sucesso.')

            return redirect('/groups')

    else:
        form = formularioGrupo()
        return render(request, 'grupos/create.html', {'form': form})

def editarGrupo(request, id):
    grupo = get_object_or_404(Grupo, pk=id)
    form = formularioGrupo(instance=grupo)

    if request.method == 'POST':
        form = formularioGrupo(request.POST, instance=grupo)

        if form.is_valid():
            grupo.save()

            messages.success(request, 'Grupo atualizado com sucesso.')

            return redirect('/groups/')
        else:
            return render(request, 'grupos/edit.html', {'form': form, 'grupo': grupo})

    else:
        return render(request, 'grupos/edit.html', {'form': form, 'grupo': grupo})

def deletarGrupo(request, id):
    grupo = get_object_or_404(Grupo, pk=id)
    grupo.delete()

    messages.info(request, 'Grupo deletado com sucesso.')

    return redirect('/groups/')
