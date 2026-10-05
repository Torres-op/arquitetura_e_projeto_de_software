class Produto:
    def preco(self):
        return 100.0

class ProdutoDecorator(Produto):
    def __init__(self, produto):
        self.produto = produto

    def preco(self):
        return self.produto.preco()

class Desconto(ProdutoDecorator):
    def preco(self):
        return self.produto.preco() * 0.9 

class Taxa(ProdutoDecorator):
    def preco(self):
        return self.produto.preco() + 20 

class Promocao(ProdutoDecorator):
    def preco(self):
        return self.produto.preco() - 10   


p = Produto()                 
p = Desconto(p)               
p = Taxa(p)                   
p = Promocao(p)               

print(p.preco())              