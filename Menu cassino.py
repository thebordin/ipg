
global user, opc
def User():
    print('Bem vindo a casa de Jogos')
    user = input('Entre com o seu nome de usuário:')
    #if BD tem usuario:
        #return user
    #else
        #Criar um usuario no DB com username, nome, contato, saldo = 1000
def Menu():
    if user != 'admin':
        print(f'Bem vindo {user}, qual vai ser a pedida de hoje?')
        print('1.Jogos')
        print('2.Estatísticas')
        print('3.Adicionar Saldo')
        opc = input('Insira sua opção')
        if opc == 1:
            return Jogos()
        elif opc == 2:
            return Estatisticas_Jogador()
        elif opc == 3:
            return Adicionar_Saldo()
        else:
          print('Opção inválida')
          return Menu()
    else:
        return Menu_Adm()
def Menu_Adm():
    print('Bem vindo Sr. Administrador')
    print('1.Estatistícas do Salão')
    print('2.Gráficos')
    print('3.Acessar jogador')
    opc = input('Insira sua opção')
    if opc == 1:
        return Estatisticas_Adm()
    elif opc == 2:
        return Graficos()
    elif opc == 3:
        return Adm_Jogador()
    else:
        print('Opção inválida')
        return Menu_Adm()

def Jogos():
    print('Blablabla')
    print('Blablabla')
    print('Blablabla')
    print('Blablabla')
    print('Blablabla')
    print('Blablabla')
    if opc == 1:
        return jogo1()
    elif opc == 2:
        return jogo2()
    elif opc == 3:
        return jogo3()
    elif opc == 2:
        return jogo4()
    elif opc == 3:
        return jogo5()
    elif opc == 2:
        return jogo6()
    else:
        print('Opção inválida')
        return Jogos()

def Estatisticas_Jogador():

def Adicionar_Saldo():
def Estatisticas_Adm():
def Graficos():
def Adm_Jogador():