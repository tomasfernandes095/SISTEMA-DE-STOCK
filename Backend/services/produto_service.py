from Backend.database.database import cursor,banco_dados
from datetime import datetime, date
from Backend.models.produtos import Produto

class ProdutoService:

    def __init__ (self, cursor, conexao):
          self.cursor = cursor
          self.conexao = conexao 

    def adicionar_produto(self):

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


                #Criar o objeto Produto
                produto = Produto(
                    codigo,
                    nome, 
                    quantidade,
                    preco,
                    validade,
                    data_formatada,
                )

                self.cursor.execute ('''
                    INSERT INTO produtos 
                    (codigo, nome, quantidade, preco, validade, data_criacao)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                          produto.codigo,
                          produto.nome,
                          produto.quantidade,
                          produto.preco,
                          produto.validade,
                          produto.data_formatada
                    ))

                self.conexao.commit()
                
                


        # //  REMOVER OS PRODUTOS   // 
    def remover_produto (self):
                remover= int (input('Escolhe o id do produto a remover: '))

                self.cursor.execute('DELETE FROM produtos WHERE id = ?', (remover,))

                self.conexao.commit()

                if self.cursor.rowcount == 0:
                    print ("Esse produto não existe")
                else:
                    print ("Removido com sucesso!")
                

    # //  VER OS PRODUTOS   // 
    def Ver_produtos (self):

            print (''' ===================== VER PRODUTOS =====================''')
                
            self.cursor.execute('SELECT id, codigo, nome, quantidade, preco FROM produtos')
            procurar = self.cursor.fetchall()

            for id, codigo, nome, quantidade, preco in procurar:

                print (f'\nId: {id}')
                print (f'Nome: {nome}')
                print (f'Quantidade: {quantidade}')
                print (f'Preco: {preco}€')



    # //  PROCURAR OS PRODUTOS   // 
    def Procurar_produtos (self):
        print (''' ===================== PROCURA DE PRODUTOS =====================''')

        codigo_produto = (input('Código do produto:'))

        self.cursor.execute('SELECT codigo, nome, quantidade, preco FROM produtos WHERE codigo = ?', (codigo_produto,))

        procurar = self.cursor.fetchone ()
        if procurar is None:
                    
            print ('Esse codigo nao existe')

        else: 
            codigo, nome, quantidade, preco = procurar

            print ('\n===================== PRODUTO ENCONTRADO =====================')
            print (f'Código:             {codigo}')
            print (f'Nome:               {nome}')
            print (f'Quantidade:         {quantidade}')
            print (f'Preco:              {preco:.2f}€ ')
            print ('===============================================================')
        


