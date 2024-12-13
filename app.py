import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_programa():
    print('''
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n
          ''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def voltar_menu_principal():
    input('\nPrecione ENTER para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(f'{texto}\n')

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                ativar_restaurante()
            case 4: # 
                finalizar_app()
    except:
        opcao_invalida()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_restaurante = input('Informe o nome do restaurante: ')
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso\n')
    restaurantes.append(nome_restaurante)
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes cadastrados')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

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