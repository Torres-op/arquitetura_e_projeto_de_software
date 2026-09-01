from dataclasses import dataclass
from enums import CategoriaProduto


@dataclass
class ItemCesta:
    nome: str
    quantidade: float
    unidade: str
    categoria: CategoriaProduto

    def __str__(self) -> str:
        return f"{self.nome}: {self.quantidade:.2f} {self.unidade} ({self.categoria.name})"
