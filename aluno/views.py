from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request,'aluno/listarAlunos.html')
    
