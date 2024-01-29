import os

restaurantes = [{'nome':'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome':'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

def exibir_mome_do_programa():
    '''Essa função exibe o nome estilizado do programa na tela'''
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
    '''Essa função exibe as opções do menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Esaa função exibe mensagem de finalização do aplicativo'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Essa função solicita que se digite uma tecla para voltar ao menu principal
    
    Inputs:
    - Tecla digitada
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Exibe mensagem de opção inválida e retorna ao menu principal
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Exibe um subtitulo
    
    Input:
    - texto: str ( O texto de cada subtitulo)
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da cagetegoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
     '''Essa função exibe uma lista contendo os restaurantes cadastrados
     
     Outputs:
     - Exibe lista de restaurantes na tela
     '''
     exibir_subtitulo('Listando os restaurantes')
     
     print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
     for restaurante in restaurantes:
         nome_restaurante = restaurante['nome']
         categoria = restaurante['categoria']
         ativo = 'ativado' if restaurante['ativo'] else 'desativado'
         print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

     voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Altera o status do restaurante ativo/desativado
    
    Outputs:
    - Exibe msg de indicando sucesso da operação'''

    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado : ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado om sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'        
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')    
    


    voltar_ao_menu_principal()

def escolher_opcao():
    '''Solicita e executa a opção escolhida pelo usuário
    
    Outputs:
    - Executa a opção selecionada pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()        

def main():
    '''Função principal que executa o programa'''
    os.system('cls')
    exibir_mome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

