from database.database import cursor
import datetime
#CRUD

#===================================
#ADICIONAR PRODUTO
#===================================

def adicionar_produto():

        codigo = str (input ('Codigo: '))
        nome = str (input('Nome do produto: '))
        quantidade = int (input('Quantidade: '))
        preco = float (input ('Preco: '))

        escreve_validade = (input('Validade: '))
        validade = datetime.datetime.strftime (escreve_validade, "%d/%m/%Y")

        # // data de criação do produto //
        data = datetime.date.today()
        data_formatada = data.strftime ("%d/%m/%Y")

        return codigo, nome, quantidade , preco , validade , data_formatada



def remover_produto ():

    remover= int (input('Escolhe o codigo do produto a remover: '))

    cursor.execute('DELETE FROM produtos WHERE id = ?', remover)
            

# //  VER OS PRODUTOS   // 

def Ver_produtos ():

      print (''' ===================== VER PRODUTOS =====================''')
      cursor.execute('WHERE nome, quantidade, preco FROM produtos')



def Procurar_produtos ():
      print (''' ===================== PROCURA DE PRODUTOS =====================''')

      codigo_produto = int (input('Código do produto:'))

      cursor.execute('WHERE ? FROM produtos ', codigo_produto)


