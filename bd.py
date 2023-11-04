import sqlite3

# Classe para lidar com o banco de dados
class BD:
    # Construtor
    def __init__(self, banco_dados):
        self.conectarBanco(banco_dados)

    # Conecta o arquivo de banco de dados e cria um suror
    def conectarBanco(self, banco_dados):
        self.banco = sqlite3.connect(banco_dados)
        self.cursor = self.banco.cursor()

        self.criarTebelaFilmes()

    def criarTebelaFilmes(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes(
                if INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                duracao TEXT NULL,
                diretor TEXT NULL,
                estudio TEXT NULL,
                classificacao TEXT NULL,
                ano DATE NULL,
            )
        """)

    def inserir(seld, tabela, valores):
        sql = f"INSERT INTO {tabela}"

        for chave, valor in valores.items():
            print(chave, valor)
            sql += f"{chave},"