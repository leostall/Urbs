# inseri a bliblioteca time (que da o tempo entre as ações (delay))
import time

# definindo as variaveis "globais"
valorPassagem = 0.00
quantidadeCreditos = 0.00
valorUltimaRecarga = 0.00
limiteUsosDia = 4
quantidadeUsada = 0
bloqueioCartao = False
senhaAdmin = '1234'


def menuPrincipal():  # função menu principal (a que escolhe o usuário)
    while True:  # loop infinito, assim a pessoa tem que escolher um tipo de usuário
        tipoUsuario = input(
            # input do tipo de usuário
            "\nComo qual tipo de usuário você deseja acessar (Usuário ou Admin)? ")

        if tipoUsuario == 'Admin':  # teste para ver se o usuario é igual a Admin
            admin()  # envia para função Admin

        elif tipoUsuario == 'Usuário':  # teste para ver se o usuario é igual a Usuário
            usuario()  # envia para função Usuario

        else:
            # Erro de reconhecimento
            print("Erro ao reconhecer o usuário! Tente novamente.")


def admin():  # variavel para as funções do Admin
    # define as variaveis que a def (função) vai usar. Caso não seja definido isso, vai dar erro no código (depois façam o teste de tirar essa linha)
    global valorPassagem, senhaAdmin, quantidadeCreditos, valorUltimaRecarga, bloqueioCartao

    while True:  # loop infinito para inserir a senha
        senhaDigitada = str(
            # pergunta a senha do admin
            input("\nPara prosseguir digite a senha do administrador. "))

        if (senhaDigitada == senhaAdmin):  # verificação se a senha inserida é igual a do admin

            # senha corresponde, então ele avisa que está na função de Admin
            print("\nVocê está na função de administrador do programa.")
            time.sleep(2)

            while True:  # loop infinito (pra sempre retornar a menu do Admin
                print("\nAtualmente a passagem custa um valor de R$",
                      valorPassagem, ".")
                time.sleep(1)

                # printa a lista de ações que o Admin pode fazer
                print("O que você deseja fazer?")
                time.sleep(2)
                print("| 1 - Alteração de valor da passagem;")
                time.sleep(0.7)
                print("| 2 - Alteração de senha de administrador;")
                time.sleep(0.7)
                print("| 3 - Verificar o valor e a última recarga no cartão;")
                time.sleep(0.7)
                print("| 4 - Desbloquear cartão;")
                time.sleep(0.7)
                print("| 5 - Sair para o menu de Usuário.")
                time.sleep(1)

                try:  # tenta fazer a ação a baixo
                    # define acao como o numero da opção que o Admin quer
                    acao = int(input("Qual opção você deseja? "))
                # caso ele retorne um ERRO, ele printa a mensagem a baixo (caso não tivesse isso, o programa ia apanas encerrar retornando um erro)
                except ValueError:
                    # printa que deu erro ao reconhecer
                    print("\nPor favor, insira um número válido.")
                    # continua o código (ou seja, volta para o menu de Admin)
                    continue

                if acao == 1:
                    try:  # se acao == 1, então ele tenta fazer a ação abaixo
                        valorPassagem = float(
                            # pergunta o valor da passagem (pode ser um numero com virgula)
                            input("\nQual o novo valor da passagem? "))
                        time.sleep(1)
                        print("Valor da passagem atualizado para: R$",
                              valorPassagem, ".")  # printa o novo valor da passagem
                        time.sleep(2)
                    except ValueError:  # caso de ERRO, ou seja, se inserir um número negativo ou um valor de texto, ele retorna o erro
                        print(
                            "Erro: Por favor, insira um valor numérico para a passagem.")  # printa o erro
                elif acao == 2:  # se acao == 2, então ele tenta fazer a ação abaixo
                    verificacaoSenha = input(
                        # pergunta a senha ATUAL do administrador
                        "\nInsira a senha de administrador ATUAL: ")
                    time.sleep(1)

                    if verificacaoSenha == senhaAdmin:  # verifica se a senha corresponde com a senha do Admin
                        novaSenha = input(
                            # se corrresponder então ele pergunta a NOVA senha
                            "Insira a NOVA senha de administrador: ")
                        # 1 - a senha não pode ser vazia "None" ou 0 (coisas que o Python considera como falso) / 2 - e se a senha NOVA for diferente da senha ANTIGA então ele atualiza a senha (ou seja, apaga a senha antiga)
                        if novaSenha and novaSenha != verificacaoSenha:
                            senhaAdmin = novaSenha  # Atualiza a senha
                            time.sleep(1)
                            print("Senha alterada com sucesso ; )")
                            time.sleep(2)
                        else:
                            print(
                                "A nova senha deve ser diferente da atual e não pode ser vazia.")
                            time.sleep(1)
                    else:  # a senha não é igual a senha do administrador
                        print("A senha não corresponde com a senha do Administrador!")
                        time.sleep(1)
                elif acao == 3:  # se acao == 3, então ele tenta fazer a ação abaixo
                    print("\nO saldo do Usuário atual é de R$",
                          quantidadeCreditos, ".")  # printa o saldo do usuário
                    time.sleep(2)
                    print("A última recarga foi no valor de R$",
                          # printa a ultima recarga (valor de recarga)
                          valorUltimaRecarga)
                    time.sleep(1)
                elif acao == 4:  # se acao == 4, então ele tenta fazer a ação abaixo
                    # se o bloqueio do carão foi True (ou seja, verdadeiro)
                    if bloqueioCartao == True:

                        print(
                            # printa a quantidade de creditos que o Usuário tem (bloqeuado no caso)
                            f"\nCartão do usuário bloqueado, com um saldo de R$", quantidadeCreditos, ".")
                        time.sleep(1)

                        desbloqueio = str(
                            # pergunta se o Admin quer desbloquear
                            input("Deseja desbloquear o cartão (Sim ou Não? "))

                        if desbloqueio == 'Sim':  # se ele digitar "Sim" no input acima, ele desbloqueia
                            bloqueioCartao = False  # desbloqueia o cartão

                            print("Cartão desbloqueado com sucesso.")
                            time.sleep(2)
                        else:  # Caso seja "Não" ou qualquer outro texto ele não desbloqueia
                            print("Negado o desbloqueio")
                            time.sleep(1)
                    # caso o cartão esteja DESBLOQUEADO, não tem como desboquear daí (né :!)
                    else:
                        print("\nO cartão do Usuário está DESBLOQUEADO!")
                        # informa a condição para bloqeuar o cartão
                        print("Somente o usuário pode bloquear o cartão!")
                        time.sleep(2)
                elif acao == 5:  # se acao == 5, então ele tenta fazer a ação abaixo
                    menuPrincipal()  # envia para o menu principal
                else:
                    # se acao não corrresponder a nenhuma opção valida (ou seja, 1, 2, 3, 4 ou 5)
                    print("Opção inválida, por favor escolha uma opção válida.")
        else:  # caso a senha de Admin esteja errada
            print("Senha incorreta, tente novamente!")


def usuario():
    # define as variaveis globais, igual no Admin
    global valorPassagem, quantidadeCreditos, valorUltimaRecarga, quantidadeUsada, limiteUsosDia, bloqueioCartao

    # informa que o Usuário está logado na função de Usuário
    print("Você está acessando o sistema como Usuário")

    # Loop infinito, pra que o Usuário possa fazer várias escolhas (sempre volta para o menu)
    while True:

        print("\nAtualmente a passagem custa um valor de R$", valorPassagem, ".")
        time.sleep(1)

        # printa as funções que o Usuário pode escolher
        print("Qual opção você deseja?")
        time.sleep(2)
        print("| 1 - Carga de créditos;")
        time.sleep(0.7)
        print("| 2 - Verificar valor e última recarga;")
        time.sleep(0.7)
        print("| 3 - Utilizar o cartão;")
        time.sleep(0.7)
        print("| 4 - Alterar limite de usos por dia;")
        time.sleep(0.7)
        print("| 5 - Bloquear cartão transporte;")
        time.sleep(0.7)
        print("| 6 - Sair para o menu de Usuário.")
        time.sleep(1)

        try:  # tenta fazer a ação abaixo
            # pega o número da ação que o Usuário escolheu
            acao = int(input("Qual opção você deseja? "))
        except ValueError:  # caso de erro, ele faz a ação abaixo
            # informa que deu erro
            print("\nPor favor, insira um número válido.")
            # continua o código (ou seja, volta para o menu (por causa do loop infinito do começo))
            continue

        if acao == 1:  # se acao == 1, então ele tenta fazer a ação abaixo
            try:  # tenta fazer a ação abaixo
                print("\nVocê atualmente possuí R$",
                      quantidadeCreditos, "em seu cartão")
                time.sleep(2)
                print("Para realizar uma recarga selecione o valor:")
                time.sleep(1)

                # printa os valores permitido para recarga
                print("| 1 - R$ 5,00;")
                time.sleep(0.5)
                print("| 2 - R$ 10,00")
                time.sleep(0.5)
                print("| 3 - R$ 15,00;")
                time.sleep(0.5)
                print("| 4 - R$ 20,00;")
                time.sleep(0.5)
                print("| 5 - R$ 30,00")
                time.sleep(0.5)
                print("| 6 - R$ 40,00")
                time.sleep(0.5)
                print("| 7 - R$ 50,00")
                time.sleep(0.5)
                print("Por motivos de segurança a recarga máxima é de R$ 50,00")
                time.sleep(2)

                try:  # tenta fazer a ação abaixo
                    # pega o número da opçõa que o Usuário escolheu
                    acao = int(input("Qual valor você deseja? "))
                except ValueError:  # caso de erro faz a ação abaixo
                    # informa o erro
                    print("\nPor favor, insira um número de opção válido.")
                    # continua o código (volta para o menu do USuário)
                    continue

                if acao == 1:  # se acao for 1 então ele chama a função recarga
                    # valorRecarga=5 (envia pela função que a variavel valorRecarga vale 5)
                    recarga(valorRecarga=5)
                elif acao == 2:  # se acao for 1 então ele chama a função recarga
                    # valorRecarga=10 (envia pela função que a variavel valorRecarga vale 10)
                    recarga(valorRecarga=10)
                elif acao == 3:  # se acao for 3 então ele chama a função recarga
                    # valorRecarga=15 (envia pela função que a variavel valorRecarga vale 15)
                    recarga(valorRecarga=15)
                elif acao == 4:  # se acao for 4 então ele chama a função recarga
                    # valorRecarga=20 (envia pela função que a variavel valorRecarga vale 20)
                    recarga(valorRecarga=20)
                elif acao == 5:  # se acao for 5 então ele chama a função recarga
                    # valorRecarga=30 (envia pela função que a variavel valorRecarga vale 30)
                    recarga(valorRecarga=30)
                elif acao == 6:  # se acao for 6 então ele chama a função recarga
                    # valorRecarga=40 (envia pela função que a variavel valorRecarga vale 40)
                    recarga(valorRecarga=40)
                elif acao == 7:  # se acao for 7 então ele chama a função recarga
                    # valorRecarga=50 (envia pela função que a variavel valorRecarga vale 50)
                    recarga(valorRecarga=50)
            except ValueError:  # caso de erro faz a ação abaixo
                print(
                    # printa o erro que aconteceu
                    "Erro: Por favor, insira um numero correspondente a opção desejada.")
        elif acao == 2:  # se acao == 2, então ele tenta fazer a ação abaixo
            # printa a quantidade de creditos
            print("\nAtualmente você possuí R$", quantidadeCreditos, ".")
            time.sleep(1)
            # printa o valor da ultima recarga feita
            print("Sua última recarga foi no valor de R$ ", valorUltimaRecarga)
            time.sleep(2)
        elif acao == 3:  # se acao == 3, então ele tenta fazer a ação abaixo
            # informa o USuário a açãoq eu selecionou
            print("\nVocê selecionou a opção de utlizar seu cartão.")
            time.sleep(1)

            quantidadePassagens = int(
                # pergunta a quantidade de passagens que deseja usar
                input("Qual a quantidade de passagens que você deseja utilizar? "))
            time.sleep(1)

            # se 0 for menor ou igual o resultado da multiplicação do valor da passagem e a quantidade menos a quantidade de creditos, então o Usuário tem dinheiro
            if 0 <= (quantidadeCreditos - (quantidadePassagens * valorPassagem)):

                # se a quantidade de passagens for menor ou igual ao limite de usos por dia menos a quantidade usada, então ele tem "limite" sobrando
                if quantidadePassagens <= (limiteUsosDia - quantidadeUsada):

                    if bloqueioCartao == False:  # se o cartão estiver desbloqueado, então ele pode usar

                        # define a quantidade de creditos como a quantidade de creditos menos a quantidade de passagens vezes o valor de cada passagem
                        quantidadeCreditos = quantidadeCreditos - \
                            (quantidadePassagens * valorPassagem)

                        # define a quantidade usada como a quantidade usada mais a quantidade de passagens selecioanda
                        quantidadeUsada = quantidadeUsada + quantidadePassagens

                        print("\nVocê utlizou", quantidadePassagens,
                              # printa quantas passagens uritlizou e o saldo atual do Usuário
                              "passagens. Seu saldo atual é de R$ ", quantidadeCreditos, ".")
                        time.sleep(2)

                    else:  # caso o cartão esteja bloqueado
                        print(
                            # printa que o  cartão está bloqueado e que o desbloqueio só pode ser feito pelo Admin
                            "\nCartão bloqueado! Ação só pode ser revertida pelo Administrador.")
                        time.sleep(2)

                else:  # caso as passagens selecionadas excedam o permitido por dia
                    # printa que as passagens foram excedidas
                    print("\nLimite de passagens excedida!")
                    time.sleep(2)

            else:  # caso o Usuário não tenha creditos suficientes
                # printa que o USuário não tem créditos
                print("\nCreditos insuficientes!")
                time.sleep(2)

        elif acao == 4:  # se acao == , então ele tenta fazer a ação abaixo
            try:  # tenta fazer a ação abaixo
                print("\nAtualmente o seu limite de usos é de:",
                      limiteUsosDia, "usos por dia.")  # printa o limite de usos por dia atuais
                time.sleep(2)

                quantidadeUsosEscolhida = int(
                    # pergunta quantas passagens por dia o usuario deseja permitir
                    input("Qual a quantidade de usos por dia você deseja? "))

                # se a quantidade escolhida for igual ou maior que 1 então faz a ação abaixo (isso significa que o Usuário não pode ter limite de: 0, -1, -2, -3 etc.)
                if (quantidadeUsosEscolhida >= 1):

                    # define o limite como a quantidade escolhida
                    limiteUsosDia = quantidadeUsosEscolhida
                    time.sleep(1)
                    # printa que foi alterado o limite
                    print("Limite alterado para", limiteUsosDia, "passagens.")
                    time.sleep(2)

                else:  # caso a quantidade escolhida seja 0 ou um valor negativo
                    # informa o erro
                    print("\nErro: Por favor, insira um numero maior ou igual a 1!")
                    time.sleep(3)

            except ValueError:  # caso de erro, retorna a ação abaixo
                # retorna que ele não inseriu um valor inteiro ou seja, ele queria um limite de 3.5 passagens (não tem como usar 0.5 da passagem)
                print("\nErro: Por favor, insira um valor inteiro!")
                time.sleep(3)

        elif acao == 5:  # se acao == 5, então ele tenta fazer a ação abaixo
            try:  # tenta fazer a ação abaixo
                # informa que o Usuário selecionou a opção de bloqueio do cartão
                print("\nATENÇÃO VOCÊ SELECIONOU A OPÇÃO DE BLOQUEIO DE CARTÃO")
                time.sleep(3)
                print(
                    # informa a condição para desbloquear o cartão
                    "Ao bloquear seu cartão somente o Administrador poderá desbloquear o cartão.")
                time.sleep(2)
                # informa o saldo do cartão
                print("Você possuí um saldo de R$", quantidadeCreditos, ".")
                time.sleep(2)

                retornoUsuario = str(
                    # recebe como string o que o Usuário digitar
                    input("Para bloquar seu cartão digite 'BLOQUEAR'. "))
                time.sleep(1)

                # se o retorno foi IDENTICO a 'BLOEQUEAR' então faz a ação abaixo (se ele digitar BLOQUEA já vai dar erro)
                if retornoUsuario == 'BLOQUEAR':
                    confirmar = int(
                        # recebe uma nova confirmação, agora com números
                        input("Deseja confirmar o bloqueio? 1 - SIM / 2 - NÃO. "))

                    if confirmar == 1:  # se receber o valor 1 então prossegue com o bloqueio
                        # define bloqueio como True (Verdadeiro)
                        bloqueioCartao = True
                        time.sleep(2)

                        # informa que o cartão foi bloqueado
                        print("\nCARTÃO BLOQUEADO")
                        time.sleep(2)
                    # se o usuário digitar QUALQUER coisa diferente de 1 (ou seja, 2, 5, 40, 25)
                    else:
                        # informa que está canecalndo a operação
                        print("Operação cancelada!")
                        time.sleep(1)
                else:  # caso o que o Usuário digitou seja diferente de BLOQUEAR
                    # printa que não reconheceu o texto
                    print("Texto não reconhecido!")
                    time.sleep(1)
            except ValueError:  # caso de erro no codigo
                # informa que deu erro
                print("Erro ao bloquear cartão, tente novaente!")
                time.sleep(1)
        elif acao == 6:  # se acao == 6, então ele tenta fazer a ação abaixo
            menuPrincipal()  # nvia para o menu que escolhe o Usuário


# Define valorRecarga como uma variavel que é enviada quando se chama a função
def recarga(valorRecarga: float):
    # informa as variaveis globais que a função usa
    global quantidadeCreditos, valorUltimaRecarga

    # informa o valor da recarga
    print("\nRecarga de R$", valorRecarga, "selecionada!")
    time.sleep(1)

    quantidadeCreditos = quantidadeCreditos + \
        valorRecarga  # Realiza a recarga do valor escolhido
    valorUltimaRecarga = valorRecarga  # Define o valor da ultima recarga

    # informa o valor atual após a recarga
    print("O valor atual do seu cartão é de R$", quantidadeCreditos, ".")
    time.sleep(1)


menuPrincipal()  # envia para o menu principal
