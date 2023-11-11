# Classe principal do programa
from interface import Interface

# Classe principal do programa 
interface = Interface()

opcao = ""

while opcao != 0:
    interface.logotipo()
    interface.mostraMenuPrincipal()
    opcao = interface.selecionaOpcao([1, 2, 0])
    interface.limpatela()

    # Tela de Cadastro de Times
    if opcao == 1:
        interface.mostraCadastroTimes()
        opcao = ""
        interface.limpatela()

    # Tela de Lista de Times
    if opcao == 2:
        interface.mostraListaTimes()
        opcao = ""
        interface.limpatela() 