from Backend.database.database import banco_dados, cursor
from Backend.services.produto_service import ProdutoService
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

    service = ProdutoService (cursor, banco_dados)
            
    if opção == 1:

        service.adicionar_produto()
        
    elif opção == 2:

        service.remover_produto()

    elif opção == 3:

        service.Ver_produtos()

    elif opção == 4: 
        service.Procurar_produtos ()
        

                        
        