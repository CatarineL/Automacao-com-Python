"""
Projeto: Sistema de Cadastro de Alunos
Você foi contratado para desenvolver um pequeno sistema de cadastro de alunos para uma escola fictícia. O sistema será usado no terminal e deve permitir que o usuário cadastre, consulte e remova alunos, além de exibir informações úteis sobre os dados inseridos.

Objetivo:
Criar um sistema simples e funcional que utilize tudo o que você aprendeu até agora em Python — como listas, dicionários, funções, loops e condicionais.

O que seu programa deve fazer:
Exibir um menu com as opções:

1. Adicionar aluno

2. Listar todos os alunos

3. Buscar aluno pelo nome

4. Remover aluno

5. Mostrar média geral das notas

6. Sair

Funcionalidades detalhadas:
Adicionar aluno
Pedir o nome, a idade e a nota (0 a 10) do aluno.

Salvar os dados em um dicionário.

Adicionar o dicionário a uma lista de alunos.

Listar todos os alunos
Mostrar todos os alunos cadastrados com nome, idade e nota.

Exibir mensagem se não houver nenhum aluno.

Buscar aluno pelo nome
Perguntar um nome e procurar na lista.

Exibir os dados se o aluno for encontrado.

Se não existir, exibir uma mensagem de erro.

Remover aluno
Perguntar o nome do aluno.

Se existir, remover da lista.

Se não existir, exibir aviso.

Média geral das notas
Calcular e exibir a média de todas as notas dos alunos cadastrados.

Se não houver alunos, exibir uma mensagem adequada.

Requisitos técnicos:
Usar listas e dicionários para armazenar os dados.

Separar funcionalidades em funções.

Usar um loop principal com menu (while True) para manter o programa rodando até o usuário sair.

Validar entradas (por exemplo: nota deve ser um número entre 0 e 10).

"""

lista_alunos = []
#funcao cadastro para inserir alunos
def cadastro():
   
   #entrada de dados
   nome = input("Digite o nome do aluno: ")
   idade = int(input("Digite a idade do aluno: "))

   #verificacao da nota
   while True:
        nota = int(input("Digite a nota do aluno: "))
        if nota >=0 and nota<=10:
            break
        else:
            print("Nota inválida. A nota deve ser de 0 a 10.")

   #dicionario de cadastro aluno
   aluno ={
      "Nome":nome,
      "Idade":idade,
      "Nota": nota
   }
   #adicionando o aluno dentro da lista 'lista_alunos'
   lista_alunos.append(aluno)

#listagem de alunos
def listar_alunos():
    if len(lista_alunos) == 0:
        print(f"Sem alunos cadastrados.")
        return
    for aluno in lista_alunos:
        print(f"Nome: {aluno['Nome']}\nIdade: {aluno['Idade']}\nNota: {aluno['Nota']}\n{'='*30}")

#pesquisa de alunos
def pesquisar_aluno(nome_aluno):
    if len(lista_alunos) == 0:
        print(f"Sem alunos cadastrados.")
        return
    for aluno in lista_alunos:
        if aluno['Nome'].lower() == nome_aluno.lower():
            print(f"Nome: {aluno['Nome']}\nIdade: {aluno['Idade']}\nNota: {aluno['Nota']}\n{'='*30}")
            break            
    else:
        print('Aluno não encontrado.')

#remover aluno
def remover_aluno(nome_alunoRe):
    if len(lista_alunos) == 0:
        print(f"Sem alunos cadastrados.")
        return
    for aluno in lista_alunos:
        if aluno['Nome'].lower() == nome_alunoRe.lower():
            lista_alunos.remove(aluno)
            print(f"Dados do aluno removido:\nNome: {aluno['Nome']}\nIdade: {aluno['Idade']}\nNota: {aluno['Nota']}\n{'='*30}")
            break            
    else:
        print('Aluno não encontrado.')

#media das notas
def media_notas():
    soma_notas=0
    if len(lista_alunos) == 0:
        print(f"Sem alunos cadastrados.")
        return
    for aluno in lista_alunos:
        soma_notas = soma_notas + aluno['Nota'] 
       
    media_final_classe = soma_notas/len(lista_alunos)
    return media_final_classe           

while True:
   
    print("\nAnalise as opções abaixo e determine qual gostaria de realizar:\n1. Adicionar aluno\n2. Listar todos os alunos\n" \
    "3. Buscar aluno pelo nome\n4. Remover aluno\n5. Mostrar média geral das notas\n6. Sair\n")

    opcao = int(input("Digite a sua opção: "))

    #case de opções
    match opcao:
        case 1:
            cadastro()
        case 2:
            listar_alunos()
        case 3:
            nome_pesquisado = input("Digite o nome do aluno: ")
            pesquisar_aluno(nome_pesquisado)
        case 4:
            nome_excluido = input("Digite o nome do aluno: ")
            remover_aluno(nome_excluido)
        case 5:
            print(media_notas())
        case 6:
            break

    

   