# FEITv, plataforma de vídeos como série e filmes.

usuarios = [['Igor','123']]
catalogo = ['Cruella','Velozes e Furiosos','Star Wars','Os vigadores','Homem areanha']


#Área de funções

#Função inicial, a qual será a primeira coisa que irá aparecer na tela
def inicial():
    print("- Bem vindo à plataforma FEITv!\n\n- Oque deseja?")
    
    #fazendo que o usuário selecione oque deseja fazer.
    opcao = int(input("- Entrar(1) \ Cadastrar(2) \ sair(3): "))
    if opcao == 1:
        loginusuario()
    if opcao == 2:
        cadastrousuario()
    if opcao == 3:
        exit()

#============================================================================================#   
    #Função de cadastrar o usuário
def cadastrousuario():
    print("- Área de cadastro:")
    nome = input("- Digite o nome do usuário: ")
    senha = input("- Digite a senha: ")

    if nome and senha: 
        usuarios.append([nome,senha]) #Erro cometido aqui, deixei o append no formato append[[]].
        print("- Usuário cadastrado com sucesso")
        inicial()
    else:
        print("- Erro ao cadastrar usuário")
        inicial()
        

#============================================================================================#
#Função de login usuário
def loginusuario():
    print("- Área de login:")
    lnome = input("- Digite o nome do usuário: ")
    
    #Campo para analisar se o usuário digitado existeR
    for i in usuarios:
        if i[0] == lnome: #Analisar a primeira coluna aonde está armazenada as informações de usuários
            lsenha = input("- Digite a senha: ")
            if i[1] == lsenha: #Analisar a segunda coluna aonde está armazenada as informações de senhas
                #Chamar a função plataforma para que o usuário possa prestigiar a plataforma.
                plataforma()
            else:
                print("- A senha está incorreta, tente novamente!")
                loginusuario()
    else:
        print("- Este usuário não existe\n")
        inicial()

#============================================================================================#


#============================================================================================#

#Função da plataforma FEITV
def plataforma():

    #função de caso o filme seja selecionado para evitar repetições
    def filme(select):
        print(f"- Filme {select} selecionado!")
        print("- Oque deseja fazer?")
        op2 = int(input("- (1) Assistir / (2) Avaliar / (3) Voltar: "))
        if op2 == 1:
            # Desenha o topo da tela de vídeo
            print("_________________________")
            print("|                       |")

            # Lógica da mensagem
            if op2 == 1:
                print("|      - Bom filme!     |")
            else:
                print("|                       |")

            # Desenha a base e os controles (play/pause)
            print("|                       |")
            print("-------------------------")
            print("  [ > ]  [ || ]  [ ■ ]   ")
            sair = int(input(" (0)Sair: "))
            if sair == 0:
                filme(select)
        if op2 == 3:
            plataforma()
            

    print("- Bem vindo ao acesso a FEITV!\n- Oque deseja?")
    op = int(input("- (1) Pesquisar por filmes / (2) Ver listas de filme / (3) Sair da Plataforma: "))

    if op == 1:
        pesquisa = int(input("- Pesquise por um filme ou série: "))
    elif op == 2:
        print("- Dê uma olhada nas listas disponíveis: ")
        #Exibe os 5 primeiros filmes/serie no catalogo
        for i in range(5):
            print(f"    -({i+1}) {catalogo[i]}")
        op1 = int(input("- Selecione um filme no catálogo: "))
        op1 = op1 - 1
        if catalogo[op1]: #Aqui vai analisar se o filme selecionado é verdadeira (Caso existe, vai ser verdadeiro)        
            select = catalogo[op1]
            filme(select)
        else: 
            print("- Filme selecionado não existe, tente novamente!")
            plataforma()
    
    elif op == 3:
        inicial()
    
        


# O Programa já inicia com a função inicial aberto.
inicial() 





