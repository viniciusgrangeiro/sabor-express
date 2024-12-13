import os

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

def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Cadastrar restaurante\n')
        case 2:
            print('Listar restaurante\n')
        case 3:
            print('Ativar restaurante\n')
        case _: # else
            finalizar_app()

def finalizar_app() :
    os.system('cls') # usado para limpar o terminal
    print('Finalizando o app\n')


def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()
    


if __name__ == '__main__':
    main()