import os

# usando o 'Dicionario', podemos adicionar varias informacoes com chave e valor a um unico indice
restaurantes = [{'nome' : 'Praça', 'categoria' : 'Japonesa', 'ativo' : False},
                {'nome' : 'Pizza Suprema', 'categoria' : 'Italiana', 'ativo' : True},
                {'nome' : 'Cantina', 'categoria' : 'Italiana', 'ativo' : False}]

def exibir_nome_programa():
    print('''
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n
          ''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar status do restaurante')
    print('4. Sair\n')

def voltar_menu_principal():
    input('\nPrecione ENTER para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(f'{texto}\n')

def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
        cadastrar_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurantes()
    elif opcao_escolhida == 3:
        alternar_status_restaurante()
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        opcao_invalida()


    # try:
    #     opcao_escolhida = int(input('Escolha uma opção: '))
    #     match opcao_escolhida:
    #         case 1:
    #             cadastrar_restaurante()
    #         case 2:
    #             listar_restaurantes()
    #         case 3:
    #             print('Ativar Restaurante')
    #             #ativar_restaurante()
    #         case 4: # 
    #             finalizar_app()
    # except:
    #     opcao_invalida()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_restaurante = input('Informe o nome do restaurante: ')
    categoria_restaurante = input(f'Informe a categoria do restaurante: ')
    novo_restaurante = {'nome' : nome_restaurante, 'categoria' : categoria_restaurante, 'ativo' : False}
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso\n')
    restaurantes.append(novo_restaurante)
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes cadastrados')

    for restaurante in restaurantes:
        nome_restaurente = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = restaurante['ativo']
        print(f'- {nome_restaurente} | {categoria_restaurante} | {status_restaurante}') 

    voltar_menu_principal()

def alternar_status_restaurante():
    exibir_subtitulo('Alternar status de restaurante')

    nome = input('Informe o nome do restaurante: ')
    encontrado = False
    
    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # Inverteu o valor que esta na chave de ativo, seja ele False ou True
            # Ternário
            mensagem = f'O Restaurante {nome} agora está ATIVO' if restaurante['ativo']  else f'O restaurante {nome} agora está DESATIVADO'
            print(mensagem)
    
    if not encontrado:
        print(f'O restaurante {nome} não foi encontrado')

    voltar_menu_principal()

def opcao_invalida():
    print('Opção inválida')
    voltar_menu_principal()

def finalizar_app() :
    exibir_subtitulo('FInalizando app')


def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()
    


if __name__ == '__main__':
    main()