from tiposdeatividade.models import TiposDeAtividade
from titulo.models import Titulo
from aluno.models import Aluno
from instrutor.models import Instrutor
from turma.models import Turma

from django.db import connection
from datetime import date
import random

#gerar numero aleatorio
def gerar_numero_aleatotio_faixa(inicio, fim):
    return random.randint(inicio, fim)


#gerar data aleatoria
def gerar_data_aleatoria(tipo_data):
    dia = gerar_numero_aleatotio_faixa(1, 28)
    mes = gerar_numero_aleatotio_faixa(1, 12)
    ano = 0

    if tipo_data == 'inicial':
        ano = gerar_numero_aleatotio_faixa(1970, 2007)
    else:
        ano = gerar_numero_aleatotio_faixa(2021, 2024) 

    return date(ano, mes, dia) 

def truncate_table(nome_tabela):

    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM {nome_tabela}')
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name = "{nome_tabela}"')

def truncar_tabelas():
    truncate_table('turma_turma')
    truncate_table('instrutor_instrutor')
    truncate_table('aluno_aluno')
    truncate_table('titulo_titulo')
    truncate_table('tiposdeatividade_tiposdeatividade')

# popular tabela com tipos de atividade
def popular_tiposdeatividade():
     lista_tiposdeatividade = []

    for i in range(1,10):
        lista_tiposdeatividade.append(TiposDeAtividade(descricao='Atividade ' + f'{i:02}'))

    TiposDeAtividade.objects.bulk_create(lista_tiposdeatividade)



def popular_titulo():
    lista_titulo = []
    for i in range(1,10):
        titulo = Titulo(descricao='Titulo' + f'{i:02}')
        lista_titulo.append(titulo)

    Titulo.objects.bulk_create(lista_titulo)       

        
         
         
        
def popular_aluno():
    Lista_aluno=[]
    for i in range(1,50):
        Lista_aluno.append(
            Aluno(
                nome= 'Aluno'+ f'{i:02}',
                data_inicial = gerar_data_aleatoria('inicial')
            )
        )
    aluno.objects.bulk_create(Lista_aluno)

def popular_instrutor():
    pass

def popular_turma():
    pass