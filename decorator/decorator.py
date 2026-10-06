from abc import ABC, abstractmethod


class Produto(ABC):
    @abstractmethod
    def preco(self) -> float:
        pass

class ProdutoBase(Produto):
    def preco(self) -> float:
        return 100.0

class ProdutoDecorator(Produto, ABC):
    def __init__(self, produto: Produto):
        self._produto = produto

    def preco(self) -> float:
        return self._produto.preco()

class Desconto(ProdutoDecorator):
    def preco(self) -> float:
        return self._produto.preco() * 0.9


class Taxa(ProdutoDecorator):
    def preco(self) -> float:
        return self._produto.preco() + 20 


class Promocao(ProdutoDecorator):
    def preco(self) -> float:
        return self._produto.preco() - 10


p: Produto = ProdutoBase()
p = Desconto(p)
p = Taxa(p)
p = Promocao(p)

print(p.preco())
