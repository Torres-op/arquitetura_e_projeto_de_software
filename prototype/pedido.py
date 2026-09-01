import calendar
import copy
from dataclasses import dataclass
from datetime import datetime
from cesta_basica import CestaBasica
from enums import TipoCliente
from prototype import Prototype


@dataclass
class Pedido(Prototype):
    cesta: CestaBasica
    tipo_cliente: TipoCliente
    data_hora_pedido: datetime
    peso_total_kg: float
    distancia_entrega_km: float

    def clonar(self) -> "Pedido":
        return copy.deepcopy(self)

    def clonar_para_proximo_mes(self) -> "Pedido":
        novo_pedido = self.clonar()
        novo_pedido.data_hora_pedido = self._somar_um_mes(self.data_hora_pedido)
        return novo_pedido

    @staticmethod
    def _somar_um_mes(data: datetime) -> datetime:
        mes = data.month + 1
        ano = data.year
        if mes > 12:
            mes = 1
            ano += 1

        ultimo_dia_do_mes = calendar.monthrange(ano, mes)[1]
        dia = min(data.day, ultimo_dia_do_mes)
        return data.replace(year=ano, month=mes, day=dia)

    def __str__(self) -> str:
        linhas = [
            f"Pedido [cliente={self.tipo_cliente.name}, "
            f"data={self.data_hora_pedido:%d/%m/%Y %H:%M}, "
            f"peso={self.peso_total_kg} kg, "
            f"distância={self.distancia_entrega_km} km]"
        ]
        for item in self.cesta.itens:
            linhas.append(f"   - {item}")
        return "\n".join(linhas)
