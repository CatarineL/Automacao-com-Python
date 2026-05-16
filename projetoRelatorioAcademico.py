'''
Seu desafio é automatizar a geração de relatórios com base no desempenho dos alunos!

Você receberá uma planilha chamada alunos.xlsx, contendo os dados de 30 alunos com as seguintes colunas:

Nome, Curso, Idade, Nota Final, Data de Matrícula

🧩 O que seu programa deve fazer:
Abrir a planilha

Percorrer todos os registros, separando os alunos em dois grupos:

Aprovados (nota final >= 7.0)

Reprovados (nota final < 7.0)

Criar dois novos arquivos Excel:

aprovados.xlsx

reprovados.xlsx

Em cada arquivo, salvar os dados completos dos respectivos alunos

Exibir no terminal:

Quantidade de aprovados e reprovados

Nota média da turma

Nome do aluno com a maior nota
'''
#biblioteca para carregar planilhas
from openpyxl import load_workbook, Workbook
from datetime import datetime


#carregamento da planilha existente
arquivo = load_workbook('alunos.xlsx')
planilha_alunos = arquivo['Alunos']


#criando uma planilha para aprovados
planilha_aprovados = Workbook()
#cursor para a planilha de aprovados
planilha_aprovados_active = planilha_aprovados.active
planilha_aprovados_active.append(['Nome', 'Curso', 'Idade', 'Nota Final', 'Data Matricula'])

#criando uma planilha para reprovados
planilha_reprovados = Workbook()
planilha_reprovados_active = planilha_reprovados.active
planilha_reprovados_active.append(['Nome', 'Curso', 'Idade', 'Nota Final', 'Data Matricula'])


#desempacotamento de dados
for linha in planilha_alunos.iter_rows(values_only=True, min_row=2, max_row=31):

    #criando variaveis para receber o valor do cabeçalho da tabela
    nome, curso, idade, nota_final, data_matricula = linha
    
    #tratamento da data de matricula
    data_matricula = data_matricula.strftime("%d/%m/%Y")
    # nome, curso, idade, nota_final, data_matricula = linha
    
    if nota_final >= 7.0: #alunos aprovados
            
        #escrevendo as linhas de aprovados na planilha de aprovados
        planilha_aprovados_active.append([nome, curso, idade, nota_final, data_matricula])
        
    elif nota_final < 7.0: #alunos reprovados
        
        #escrevendo as linhas de aprovados na planilha de reprovados
        planilha_reprovados_active.append([nome, curso, idade, nota_final, data_matricula])

#salvando os dados
planilha_aprovados.save('PlanilhaAprovados.xlsx')
planilha_reprovados.save('PlanilhaReprovados.xlsx')