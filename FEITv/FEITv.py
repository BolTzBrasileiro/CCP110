# FEITv, plataforma de vídeos como série e filmes.

usuarios = []


def inicial():
    print("Bem vindo à plataforma FEITv!\n\nOque deseja?")
    
    #fazendo que o usuário selecione oque deseja fazer.
    opcao = int(input("-Entrar(0) \ Cadastrar(1) \ sair(2): "))
    if opcao == 1:
        cadastrousuario()
    if opcao == 2:
        exit()
        
    #Função de cadastrar o usuário
def cadastrousuario():

    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    if nome and senha: 
        usuarios.append([nome,senha]) #Erro cometido aqui, deixei o append no formato append[[]].
        print("Usuário cadastrado com sucesso")
        inicial()
    else:
        print("Erro ao cadastrar usuário")
        inicial()


inicial()





