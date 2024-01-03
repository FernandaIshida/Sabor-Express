import os

def exibir_mome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_mome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

