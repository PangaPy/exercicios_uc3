from django.shortcuts import redirect, render
from titulo.forms import TituloForm
from titulo.models import Titulo
from instrutor.models import Instrutor

# Create your views here.
def listar(request):

    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulos
    }

    return render(request, 'titulo/listarTitulos.html', context=contexto)

def cadastro(request):
    return render(request, 'titulo/cadastroTitulos.html')

def cadastrar(request):
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Titulo(descricao = dados_titulo['descricao']
        )
        titulo.save()

    return render(request, 'titulo/cadastroTitulos.html')

def excluir(request, codigo):
    titulo = Titulo.objects.get(pk=codigo)

    instrutores = Instrutor.objects.filter(codigo_titulo=codigo)
    if not instrutores: 
        titulo.delete()

    return redirect('titulo:listar')
