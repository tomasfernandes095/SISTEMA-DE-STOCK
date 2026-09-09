from database.database import banco_dados, cursor
from produtos.produtos import produto


#===================================
#MENU
#===================================

while True:

    print ("""    ========================================
                SISTEMA DE STOCK
    ========================================  

            [ 1 ] Adicionar produto
            [ 2 ] Remover produto
            [ 3 ] Ver produtos
                        """)


    opção = int (input('\nEscolhe uma opção: '))

    if opção == 1:

        adicionar = produto.adicionar_produto()
        cursor.execute ("""INSERT INTO produtos 
        (codigo, nome, quantidade, preco, validade, data_criacao )
        VALUES(:codigo, :nome, :quantidade, :preco, :validade, :data_formatada)""", adicionar)

        banco_dados.commit()
        
        
    elif opção == 2:

        adicionar.remover_produto()

    elif opção == 3:

        adicionar.Ver_produtos()
        

                        
        