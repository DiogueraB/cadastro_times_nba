import os
from bd import BD

class Interface:
    # Construtor
    def __init__(self):
        self.banco = BD("timesNBA.db")

    def logotipo(self):                                                 
        print()
        print("            _   _   ____     ___              ")
        print("           | \ | | |  _ \   / _ \             ")
        print("           |  \| | | |_) ) | |_| |            ")
        print("           |     | |  _ (  |  _  |            ")
        print("           | |\  | | |_) ) | | | |            ")
        print("           |_| \_| |____/  |_| |_|            ")
        print("                                              ")
        print("                                              ")     

    def limpatela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Função que permite o usuário escolher uma opção
    # opcoes = []
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

        nome = self.solicitaValor('Digite o nome do time*: ', 'texto', False)
        fundacao = self.solicitaValor('Digite o ano da fundação*: ', 'texto', False)
        fundador = self.solicitaValor('Digite o nome do fundador: ', 'texto', True)
        cidade = self.solicitaValor('Digite onde se localiza o time: ', 'texto', False)
        arena = self.solicitaValor('Digite o nome da arena: ', 'texto', True)  
        mascote = self.solicitaValor('Digite o nome do mascote: ', 'texto', True)
        campeonatos = self.solicitaValor('Digite quantos campeonatos foram ganhos: ', 'texto', True)

        # Armazena os valores no banco de dados!
        valores = {
            "nome": nome,
            "fundacao": fundacao,
            "fundador": fundador,
            "cidade": cidade,
            "arena": arena,
            "mascote": mascote,
            "campeonatos": campeonatos
        }
        self.banco.inserir('times',valores)

    def mostraListaTimes(self):
        self.logotipo()

        print("Veja abaixo a lista de Times da NBA cadastrados.")
        print()

        times = self.banco.buscaDados('times')

        for time in times:
            #print(time)
            id, nome, fundacao, fundador, cidade, arena, mascote, campeonatos = time

            print(f"Time {id} - {nome} | {fundacao}")
            print()

        input("Aperte Enter para continuar...") 

    # Solicita um valor do usuário e valida ele
    # Return valordigitado
    def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
        valor = input(legenda)

        # Verifica se está vazio
        if valor == "" and not permiteNulo:
            print("Valor inválido!")
            return self.solicitaValor(legenda, tipo,permiteNulo)
        elif valor == "" and permiteNulo:
            return valor

        # Verifica se está no formato correto
        if tipo == 'numero':
            try: 
                valor = float(valor)
            except ValueError:
                print("Valor Inválido!")
                return self.solicitaValor(legenda, tipo, permiteNulo)
            
        return valor