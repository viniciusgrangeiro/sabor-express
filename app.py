import os

# usando o 'Dicionario', podemos adicionar varias informacoes com chave e valor a um unico indice
restaurantes = [{'nome' : 'Praça', 'categoria' : 'Japonesa', 'ativo' : False},
                {'nome' : 'Pizza Suprema', 'categoria' : 'Italiana', 'ativo' : True},
                {'nome' : 'Cantina', 'categoria' : 'Italiana', 'ativo' : False}]

def exibir_nome_programa():
    '''Essa função imprime o nome do programa'''

    print('''
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n
          ''')

def exibir_opcoes():
    '''Essa função apenas imprime opções para o menu principal'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar status do restaurante')
    print('4. Sair\n')

def voltar_menu_principal():
    '''Esta função retorna para o menu inicial, e aparece sempre após uma iteração finalizada do usuario'''

    input('\nPrecione ENTER para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    '''Essa função exibe um subtitulo estilizado com *s que se alinha com o tamanho do subtitulo
    
    Inputs:
    - Subtitulo a ser exibido

    Output:
    - Texto com os asteriscos envolta 
    '''
    os.system('cls')
    # Escreve * vezes a quantidade de caracteres que existem no texto
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(f'{linha}\n')

def escolher_opcoes():
    '''Recebe a opção escolhida pelo usuario no menu e
    aplica a função escolhida pelo usuario
    
    Input:
    - Opcao que o usuario deseja

    Output:
    - É redirecionado para a função desejada
    '''

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
    '''Cadastra novos restaurantes
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Output:
    - Cadastra novo restaurante na lista de restaurantes
    '''
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_restaurante = input('Informe o nome do restaurante: ')
    categoria_restaurante = input(f'Informe a categoria do restaurante: ')
    novo_restaurante = {'nome' : nome_restaurante, 'categoria' : categoria_restaurante, 'ativo' : False}
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso\n')
    restaurantes.append(novo_restaurante)
    voltar_menu_principal()

def listar_restaurantes():
    '''Lista todos os restaurantes que estao guardados no dicionario
    e imprime de forma listada'''

    exibir_subtitulo('Listando restaurantes cadastrados')
    print(f'{'Nome'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurente = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = 'atvado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurente.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante}') #.ljust(quanto de espacamento) 

    voltar_menu_principal()

def alternar_status_restaurante():
    '''Ativa ou desativa restaurantes
    
    Input:
    - Nome do restaurante

    Output:
    - Informa que o status do restaurante foi alterado
    - Informa que o restaurante não foi encontrado
    '''
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
    '''Esta função chama o aplicativo em sua totalidade'''
    
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()
    


if __name__ == '__main__':
    main()