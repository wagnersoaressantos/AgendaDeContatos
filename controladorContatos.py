listaContatos=[]
telefoneTemporario=[]
numeroTelefone=[]
def cadastrarContato():
    print("*****CADASTRAR CONTATO****")
    while True:
        nome = input("Digite nome: ")
        sobrenome = input("Digite o sobrenome: ")
        nomeSobrenome =[nome,sobrenome]
        while True:
            telefone=int(input("Digite telefone:"))
            if checarNumero(telefone):
                print("Telefone já cadastrado!")
                input("Click em enter para retornar au menu!!!")
                return
            elif checarNumeroTemporaril(telefone):
                print("Telefone já cadastrado!")
                input("Click em enter para retornar au menu!!!")
                return
            opcao = int(input("Deseja cadastro outro número? [1] - Sim;[2] - Não:\n"))
            print("opção: ", opcao)
            numeroTelefone.append(telefone)
            telefoneTemporario.append(telefone)
            if opcao != 1:
                break
        endereco=input("Digite o endereço:")
        contato=[nomeSobrenome,numeroTelefone,endereco]
        listaContatos.append(contato)
        while len(telefoneTemporario)>0:
            telefoneTemporario.pop()
        opcao=int(input("Deseja fazer outro cadastro? [1] - Sim;[2] - Não:\n"))
        print("opção: ",opcao)
        if opcao != 1:
            break
def checarNumero(telefone):
    cadastrarContato=False
    for i in range(0, len(numeroTelefone)):
        if telefone==numeroTelefone[i]:
            print("entrou na checagem da listaContatos")
            cadastrarContato=True
    return cadastrarContato
def checarNumeroTemporaril(telefone):
    cadastrarContato=False
    for i in range(0,len(telefoneTemporario)):
        if telefone==telefoneTemporario[i]:
            print("entrou na checagem de telefoneTemporario")
            cadastrarContato=True
    return cadastrarContato


def listaDeContatos():
    print("\n")
    print("*****LISTA DE CONTATOS*****")
    for i in range (0, len(listaContatos)):
        print("Nome: ",listaContatos[i][0][0])
        print("Sobrenome: ", listaContatos[i][0][1])
        print("Telefone: ", listaContatos[i][1])
        print("Endereço: ", listaContatos[i][2])
    input("Click em enter para voltar ao menu!!")
    return

def editarOuRemoverContato():
    print("\n")
    print("*****EDITAR OU REMOVER CONTATO*****")
    Nome=input("Informe o nome: ")
    for i in range(0, len(listaContatos)):
        if listaContatos[i][0][0]==Nome:
            print("Deseja Remover ou Editar o cadastros do Aluno:")
            print("Nome: ", listaContatos[i][0][0])
            print("Sobrenome: ", listaContatos[i][0][1])
            print("Telefone: ", listaContatos[i][1])
            opcao = int(input("Digite:\n[1]- PARA EDITAR \nou\n[2]- PARA REMOVER\nOpção: "))
            if opcao == 1:
                print("*****EDITAR CADASTRO*****")
                print("Do contato: ", listaContatos[i][0][0])
                confirmacao = int(input("\nDeseja editar o cadastro:\n[1]-SIM\n[2]-NÃO\nQual opção?"))
                if confirmacao == 1:
                    editar=int(input("\nGosta de editar oque:\n[1]-Número\n[2]-Nome\nqual opção?"))
                    if editar==1:
                        print("Editar telefone")
                        print("De", listaContatos[i][0][0])
                        novoNumero=input("\nDigite a novo número: ")
                        print("Número antigo: ", listaContatos[i][1])
                        listaContatos[i][1]=novoNumero
                        print("Novo número: ", listaContatos[i][1])
                    elif editar==2:
                        print("editar Nome")
                        novoNome = input("\nDigite a novo nome: ")
                        print("Nome antigo: ", listaContatos[i][0][0])
                        listaContatos[i][0][0] = novoNome
                        print("Nova nome: ", listaContatos[i][0][0])
                    input("Clik enter para retorna ao menur!!")
            elif opcao==2:
                print("*****REMOVER CADASTRO*****")
                print("Do contato: ", listaContatos[i][1])
                confirmacao=int(input("\nconfimar a exclusão:\n[1]-SIM\n[2]-NÃO\nQual opção?"))
                if confirmacao==1:
                    listaContatos.pop(i)
                    print("Cadastro excluido!!")
                    input("Clik enter para retorna ao menur!!")
                return
            return
    print("contato não encontrado!!!")
    input("click em entre para retorna ao menu!!!")