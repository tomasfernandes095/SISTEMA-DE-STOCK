from database.database import banco_dados, cursor
from produtos.produtos import adicionar_produto
#===================================
#MENU
#===================================
while True:

    print ("""    ========================================
                SISTEMA DE STOCK
    ========================================  

            [ 1 ] Adicionar produto 
                        """)


    opção = int (input('\nEscolhe uma opção: '))

    if opção == 1:
        adicionar = adicionar_produto()
        cursor.execute ("""INSERT INTO produtos 
        (codigo, nome, quantidade, preco, validade, data_criacao )
        VALUES(?, ?, ?, ?, ?, ?)""", adicionar)

        banco_dados.commit()
     
        print ('Produto guardado com sucesso')