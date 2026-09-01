from dataclasses import dataclass, field
from typing import List
from item_cesta import ItemCesta
from enums import CategoriaProduto


@dataclass
class CestaBasica:
    itens: List[ItemCesta] = field(default_factory=list)

    def adicionar_item(self, item: ItemCesta) -> None:
        self.itens.append(item)

    def substituir_quantidade(self, nome_item: str, nova_quantidade: float) -> None:
        for item in self.itens:
            if item.nome.lower() == nome_item.lower():
                item.quantidade = nova_quantidade
                return

    @staticmethod
    def montar_cesta_padrao() -> "CestaBasica":
        cesta = CestaBasica()

        cesta.adicionar_item(ItemCesta("Picanha", 6, "kg", CategoriaProduto.ORIGEM_ANIMAL))
        cesta.adicionar_item(ItemCesta("Leite", 7.5, "litros", CategoriaProduto.ORIGEM_ANIMAL))

        cesta.adicionar_item(ItemCesta("Arroz", 3, "kg", CategoriaProduto.GRAOS))
        cesta.adicionar_item(ItemCesta("Feijão", 4.5, "kg", CategoriaProduto.GRAOS))
        cesta.adicionar_item(ItemCesta("Farinha", 1.5, "kg", CategoriaProduto.GRAOS))

        cesta.adicionar_item(ItemCesta("Café", 0.6, "kg", CategoriaProduto.INDUSTRIALIZADOS))
        cesta.adicionar_item(ItemCesta("Óleo", 0.9, "litros", CategoriaProduto.INDUSTRIALIZADOS))
        cesta.adicionar_item(ItemCesta("Manteiga", 0.75, "kg", CategoriaProduto.INDUSTRIALIZADOS))
        cesta.adicionar_item(ItemCesta("Açúcar", 3, "kg", CategoriaProduto.INDUSTRIALIZADOS))

        cesta.adicionar_item(ItemCesta("Batata", 6, "kg", CategoriaProduto.LEGUMES_E_FRUTAS))
        cesta.adicionar_item(ItemCesta("Cenoura", 9, "kg", CategoriaProduto.LEGUMES_E_FRUTAS))
        cesta.adicionar_item(ItemCesta("Maçã", 7.5, "dúzias", CategoriaProduto.LEGUMES_E_FRUTAS))

        return cesta
