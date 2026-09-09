from database.database import cursor,banco_dados
from datetime import datetime, date


#CRUD

#===================================
#ADICIONAR PRODUTO
#===================================

class produto:
      def adicionar_produto():

            codigo = str (input ('Codigo: '))
            nome = str (input('Nome do produto: '))
            quantidade = int (input('Quantidade: '))
            preco = float (input ('Preco: '))

            # // validade 
            escreve_validade = (input('Introduza a validade (DD/MM/AAAA): '))
            validade = datetime.strptime (escreve_validade, "%d/%m/%Y")
            validade = validade.strftime ("%d/%m/%Y")

            # // data de criação do produto //
            data = date.today()
            data_formatada = data.strftime ("%d/%m/%Y")

            print ('\n=================PRODUTO=================')
            print (f'\n Código: {codigo} | Nome: {nome} | Quantidade: {quantidade} | Preço: {preco} | Validade: {validade}')
            print ('\033[3;30m Foi criado com sucesso!\033[m')

            produto = { 
                  "codigo": codigo, 
                  "nome": nome,
                  "quantidade": quantidade,
                  "preco": preco,
                  "validade": validade,
                  "data_formatada": data_formatada
            }
            return produto
            


      # //  REMOVER OS PRODUTOS   // 
      def remover_produto ():
            remover= int (input('Escolhe o id do produto a remover: '))
            cursor.execute('DELETE FROM produtos WHERE id = ?', (remover,))

            banco_dados.commit()

      if cursor.rowcount == 0:
            print ("Esse produto não existe")
      else:
            print ("Removido com sucesso!")
            

      

      
                  


      # //  VER OS PRODUTOS   // 
      def Ver_produtos ():

            print (''' ===================== VER PRODUTOS =====================''')
            
            cursor.execute('WHERE id, nome, quantidade, preco FROM produtos')



      # //  PROCURAR OS PRODUTOS   // 
      def Procurar_produtos ():
            print (''' ===================== PROCURA DE PRODUTOS =====================''')

            codigo_produto = int (input('Código do produto:'))

            cursor.execute('WHERE codigo = ? FROM produtos ', codigo_produto)

      


