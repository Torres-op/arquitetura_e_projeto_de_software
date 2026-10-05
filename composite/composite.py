from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def tamanho(self):
        pass

    @abstractmethod
    def mostrar(self, indent=""):
        pass

class Arquivo(Item):
    def __init__(self, nome, tamanho):
        super().__init__(nome)
        self._tamanho = tamanho

    def tamanho(self):
        return self._tamanho

    def mostrar(self, indent=""):
        print(f"{indent}- {self.nome} ({self.tamanho()} bytes)")

class Pasta(Item):
    def __init__(self, nome):
        super().__init__(nome)
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def tamanho(self):
        return sum(item.tamanho() for item in self.itens)

    def mostrar(self, indent=""):
        print(f"{indent}+ {self.nome} ({self.tamanho()} bytes)")
        for item in self.itens:
            item.mostrar(indent + "   ")


raiz = Pasta("C:")
raiz.adicionar(Arquivo("foto.jpg", 200))
raiz.adicionar(Arquivo("leiame.txt", 10))

docs = Pasta("Documentos")
docs.adicionar(Arquivo("contrato.txt", 50))
raiz.adicionar(docs)

raiz.mostrar()