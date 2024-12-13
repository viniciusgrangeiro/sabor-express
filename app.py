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
    # print(f'Você escolheu a opção {opcao_escolhida}')
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
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