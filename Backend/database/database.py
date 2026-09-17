import sqlite3

banco_dados = sqlite3.connect ("Backend/database/stock.db") #Banco de dados

cursor = banco_dados.cursor() #Só da para fazer operações se usar o cursor

cursor.execute ("CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, codigo TEXT, nome TEXT, quantidade INTEGER, preco REAL, validade TEXT, data_criacao TEXT)")
cursor.execute ("CREATE TABLE IF NOT EXISTS utilizadores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL, cargo TEXT NOT NULL)")

banco_dados.commit()