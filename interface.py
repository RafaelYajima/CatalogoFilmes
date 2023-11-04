import os
from bd import BD

# Classe para interface do usuario do programa
class Interface:
    # Construtor
    def __init__(self):
        self.banco = BD("catalogoFilmes.db")
    
    def logoTipo(self):
        print()
        print("============================")
        print("=====Catalogo de Filmes=====")
        print("============================")
        print()

    def limpaTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Função que permite o usuario escolher uma opção
    # opçoes = []
    def selecionaOpcao(self, opcoesPermitidas = []):
        opcaoSelecionada = input("Digite a opção desejada: ")

        # Verifica se digitou algo
        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcoesPermitidas)
            
        # Tenta converter para numero
        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("Opção invalida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Verifica se a opção selecionada é valida
        if opcaoSelecionada not in opcoesPermitidas:
            print("Opção invalida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Retorna o valor selecionado pelo usuario
        return opcaoSelecionada
    
    # Mostra menu principal do sistema
    def mostraMenuPrincipal(self):
        print("1 - Cadastrar filme")
        print("2 - Lista de filmes")
        print("0 - Sair")
        print()

    def mostraCadastroFilmes(self):
        self.logoTipo()

        print("Insira os dados do filme:")
        print("(campos com * são obrigatorios)")

        titulo = self.solicitaValor('Nome do titulo: ', 'texto', False)
        genero = self.solicitaValor('Qual gênero: ', 'texto', False)
        duracao = self.solicitaValor('Duração do filme: ', 'texto', True)
        diretor = self.solicitaValor('Nome do diretor: ', 'texto', True)
        estudio = self.solicitaValor('Nome do estudio: ', 'texto', True)
        classificacao = self.solicitaValor('Qual a classificação: ', 'texto', True)
        ano = self.solicitaValor('Ano do filme: ', 'texto', True)

        # Armazena os valores no banco de dados!
        valores = {
            "titulo": titulo,
            "genero": genero,
            "duracao": duracao,
            "diretor": diretor,
            "estudio": estudio,
            "classificacao": classificacao,
            "ano": ano,
        }
        self.banco.inserir('filmes',)

    # Solicita um valor do usuario e valida ele
    def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
        valor = input(legenda)

        # Verifica se eata vazio
        if valor == "" and not permiteNulo:
            print("Valor invalido!")
            return self.solicitaValor(legenda, tipo, permiteNulo)
        elif valor == "" and permiteNulo:
            return valor
        
        # verifica se esta no formato correto
        if tipo == 'numero':
            try:
                valor = float(valor)
            except ValueError:
                print("Valor invalido!")
                return self.solicitaValor(legenda, tipo, permiteNulo)
        return valor