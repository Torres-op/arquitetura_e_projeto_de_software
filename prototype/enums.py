from enum import Enum, auto


class CategoriaProduto(Enum):
    ORIGEM_ANIMAL = auto()
    GRAOS = auto()
    INDUSTRIALIZADOS = auto()
    LEGUMES_E_FRUTAS = auto()


class TipoCliente(Enum):
    FAMILIA_CADASTRADA = auto()
    IDOSO = auto()
    GESTANTE = auto()
    PESSOA_COM_DEFICIENCIA = auto()
