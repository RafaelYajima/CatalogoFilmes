# Importa a classe interface
from interface import Interface

# Classe principal do programa
interface = Interface()

opcao = ""
while opcao != 0:
    interface.logoTipo()
    interface.mostraMenuPrincipal()
    interface.selecionaOpcao([1, 2, 0])
    interface.limpaTela()

    # Tela de cadastro de filmes
    if opcao == 1:
        interface.mostraCadastroFilmes()

    # Tela de lista de filmes
    if opcao == 2:
        pass

    