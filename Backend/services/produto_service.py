from datetime import datetime, date
from Backend.models.produtos import Produto
import time
from rich import print
from rich.live import Live
from rich.emoji import Emoji


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

        codigo_produto = input('Código do produto:')

        self.cursor.execute('SELECT codigo, nome, quantidade, preco FROM produtos WHERE codigo = ?', (codigo_produto,))

        procurar = self.cursor.fetchone ()
            
        if procurar is None:
                    
            print ('Esse codigo nao existe')

        else: 
            codigo, nome, quantidade, preco = procurar

            print ('\n\n===================== PRODUTO ENCONTRADO =====================')
            print (f'Código:             {codigo}')
            print (f'Nome:               {nome}')
            print (f'Quantidade:         {quantidade}')
            print (f'Preco:              {preco:.2f}€ ')
            print ('===============================================================')



    def Alterar_produto (self):

        while True:

            animacao_pontos = [
                            "[blink].  [/blink]",
                            "[blink].. [/blink]",
                            "[blink]...[/blink]"
                                ]
            
            # O Live mantém o terminal atualizado no mesmo lugar
            with Live("", refresh_per_second=3) as live:
             # Simula uma tarefa que demora 6 segundos
                for i in range(6):
                # Altera o texto a cada segundo usando o operador resto (%)
                    ponto_atual = animacao_pontos[i % len(animacao_pontos)]
                    live.update(f"Inicializando {ponto_atual}")
                    time.sleep(0.5)

        
            print ('\n[bold blue][ 0 ] Encerrar sistema [/bold blue]')
            produto_alterar = input ('Código do produto (DIGITE 0 PARA ENCERRAR O SISTEMA): ')
            
            self.cursor.execute ('SELECT codigo, nome, quantidade, preco FROM produtos WHERE codigo = ?', (produto_alterar,))

            encontrar = self.cursor.fetchone()

            if produto_alterar == '0':
                print  ('Obrigado por usar :thumbs_up: ')
                break

        
            animacao_pontos = [
                "[blink].  [/blink]",
                "[blink].. [/blink]",
                "[blink]...[/blink]"
                    ]

            # O Live mantém o terminal atualizado no mesmo lugar
            with Live("", refresh_per_second=3) as live:
             # Simula uma tarefa que demora 6 segundos
                for i in range(6):
                # Altera o texto a cada segundo usando o operador resto (%)
                    ponto_atual = animacao_pontos[i % len(animacao_pontos)]
                    live.update(f"A procurar produto {ponto_atual}")
                    time.sleep(0.5)

            if not encontrar:
                print ('[bold red]Este código nao existe[/]\n')
                
            else:
                codigo, nome, quantidade, preco= encontrar

                print ('\n\n===================== PRODUTO ENCONTRADO =====================')
                print (f'Código:             {codigo}')
                print (f'Nome:               {nome}')
                print (f'Quantidade:         {quantidade}')
                print (f'Preco:              {preco:.2f}€ ')
                print ('===============================================================')
                

                
                Escolha =str(input('Deseja alterar o produto (S/N)?'))

            try:

                if Escolha.lower() not in ('s', 'sim'):
                    print ('[green]Sem alteraçoes[/green]')
                    print ('')                            
                           
                else:               
                    while True:

                        print ('\n===================== ALTERAR PRODUTO =====================')                
                        print ('                     [ 1 ] Alterar codigo')
                        print ('                     [ 2 ] Alterar Nome')
                        print ('                     [ 3 ] Alterar preco')
                        print ('                     [bold blue][ 0 ] Voltar [/bold blue]      ')
                        print ('===============================================================')              
                        opcao =int(input('Escolhe o numero da função que queres alterar: '))

                        if opcao == 1:
                            codigo_novo = int(input('Qual o código novo do produto: '))
                            self.cursor.execute ('UPDATE produtos SET codigo = ? WHERE codigo = ?', (codigo_novo, produto_alterar))
                            self.conexao.commit () 
                            print (f'\n\nAlteraste o codigo: {produto_alterar} | Ficando: {codigo_novo}')

                        elif opcao == 2:
                            nome_novo = str(input('Qual o nome novo do produto: '))
                            self.cursor.execute ('UPDATE produtos SET nome = ? WHERE codigo = ?', (nome_novo, produto_alterar))
                            self.conexao.commit () 
                            print (f'\n\nAlteraste o codigo: {nome} | Ficando: {nome_novo}')

                        elif opcao == 3:
                            preco_novo =str(input('Qual preço novo do produto: '))

                            preco_final = preco_novo.replace('R$','').replace('€','').replace('$','')
                            preco_final = float(preco_final)
                            self.cursor.execute ('UPDATE produtos SET preco = ? WHERE codigo = ?', (preco_final, produto_alterar))
                            self.conexao.commit () 
                            print (f'\n\nAlteraste o codigo: {preco} | Ficando: {preco_novo}')

                        elif opcao == 0:
                            print  ('Obrigado por usar :thumbs_up: ')
                            break

            except:
                  print (f'ERRO: Escreve um numero ou uma letra')
                    

                
