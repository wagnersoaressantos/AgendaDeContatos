from menuContatos import menu
from controladorContatos import*
def main():
    while True:
        opcaoMenur=menu()
        if opcaoMenur ==1:
            print("[1]-ADICIONAR CONTATO")
            cadastrarContato()
        elif opcaoMenur ==2:
            print("[2]-LISTA DE CONTATOS")
            listaDeContatos()
        elif opcaoMenur ==3:
            print("[3]-EDITAR OU REMOVER CONTATO")
            editarOuRemoverContato()
        elif opcaoMenur ==4:
            print("Finalizando programa!!!")
            break
        else:
            print("Opção invalida!!!")
            print("Escolha de novo!!!")
            input()
main()
