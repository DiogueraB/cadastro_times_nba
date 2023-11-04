import os

class Interface:
    # Construtor
    def __init__(self):
        pass

    def logotipo(self):                                                 
        print ()    
        print ("                                   _______   _                              _   _   ____                                             ")
        print ("      ______   ______   ______    |__   __| (_)                            | \ | | |  _ \      /\        ______   ______   ______    ")
        print ("     |______| |______| |______|      | |     _   _ __ ___     ___   ___    |  \| | | |_) |    /  \      |______| |______| |______|   ")
        print ("      ______   ______   ______       | |    | | | '_ ` _ \   / _ \ / __|   | . ` | |  _ <    / /\ \      ______   ______   ______    ")
        print ("     |______| |______| |______|      | |    | | | | | | | | |  __/ \__ \   | |\  | | |_) |  / ____ \    |______| |______| |______|   ")
        print ("                                     |_|    |_| |_| |_| |_|  \___| |___/   |_| \_| |____/  /_/    \_\                                ")


    def limpatela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def selecionaOpcao(self,  opcoesPermitidas = []):
        opcaoSelecionada = input("Digite a opção desejada: ")

        # Verifica se digitou algo
        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcoesPermitidas)
            
        # Tenta converter para números
        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)
            
        # Verifica se a opção selecionada é uma das opções válidas
        if opcaoSelecionada not in opcoesPermitidas:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Retorna o valor selecionado pelo usuário 
        return opcaoSelecionada

    def mostraMenuPrincipal(self):
        print ()
        print ("1 - Cadastrar Times NBA ")
        print ("2 - Lista Times Cadastrados ")
        print ("0 - Sair")
        print ()

    def mostraCadastroTimes(self):
        self.logotipo()

        print("Insira os dados do Time:")
        print("(Campos com * são obrigatórios)")

        nome = self.solicitaValor('Digite o nome: ', 'texto', False)
        fundacao = self.solicitaValor('Digite o ano da fundação: ', 'texto', False)
        fundador = self.solicitaValor('Digite o nome do fundador: ', 'texto', False)
        cidade = self.solicitaValor('Digite onde se localiza o time: ', 'texto', False)
        arena = self.solicitaValor('Digite o nome da arena: ', 'texto', False)  
        mascote = self.solicitaValor('Digite o nome do mascote: ', 'texto', False)
        campeonatos = self.solicitaValor('Digite quantos campeonatos foram ganhos: ', 'texto', False)