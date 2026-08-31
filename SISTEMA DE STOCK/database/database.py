import sqlite3

banco_dados = sqlite3.connect ("database.db") #Banco de dados

cursor = banco_dados.cursor() #Só da para fazer operações se usar o cursor


cursor.execute ("CREATE TABLE IF NOT EXISTS produtos(id INTEGRE PRIMARY KEY, codigo TEXT, nome TEXT, quantidade INTEGER, preco REAL, validade TEXT, data_criacao TEXT)")

banco_dados.commit()