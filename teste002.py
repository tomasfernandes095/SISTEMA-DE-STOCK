from Backend.database.database import banco_dados, cursor

Encontrar = (input ('Qual o produto que queres procurar: '))

cursor.execute("SELECT codigo, nome, quantidade, preco FROM produtos WHERE codigo = ?", (Encontrar,))

produto = cursor.fetchone () 

if produto is None:
    print('Esse código não existe')
else:
    print('Este é o produto que procura:')
    print(produto)
