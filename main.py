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

    if opcao == 1:
        interface.mostraCadastroTimes()
        opcao = ""
        interface.limpatela()

    if opcao == 2:
        pass