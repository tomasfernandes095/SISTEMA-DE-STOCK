from Backend.services.produto_service import ProdutoService
from Backend.database.database import cursor, banco_dados

f= ProdutoService (cursor, banco_dados)

f.Alterar_produto ()

