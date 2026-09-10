from Backend.database.database import banco_dados, cursor
from Backend.produtos.produtos import Produto
import time

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
            [ 4 ] Procurar produtos
                        """)


    opção = int (input('\nEscolhe uma opção: '))

    if opção == 1:

        adicionar = Produto.adicionar_produto()
        
        cursor.execute ("""INSERT INTO produtos 
        (id, codigo, nome, quantidade, preco, validade, data_criacao )
        VALUES(:codigo, :nome, :quantidade, :preco, :validade, :data_formatada)""", 
        {
            "codigo": adicionar.codigo,
            "nome": adicionar.nome,
            "quantidade": adicionar.quantidade,
            "preco": adicionar.preco,
            "validade": adicionar.validade,
            "data_formatada": adicionar.data_formatada
        })
        time.sleep (3)
        banco_dados.commit()
        
        
    elif opção == 2:

        Produto.remover_produto()

    elif opção == 3:

        Produto.Ver_produtos()

    elif opção == 4: 
        Produto.Procurar_produtos ()
        

                        
        