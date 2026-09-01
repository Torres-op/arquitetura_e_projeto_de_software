from datetime import datetime
from cesta_basica import CestaBasica
from enums import TipoCliente
from pedido import Pedido


def main() -> None:
    cesta_padrao = CestaBasica.montar_cesta_padrao()

    pedido_agosto = Pedido(
        cesta=cesta_padrao,
        tipo_cliente=TipoCliente.FAMILIA_CADASTRADA,
        data_hora_pedido=datetime(2026, 8, 5, 9, 0),
        peso_total_kg=40.0,
        distancia_entrega_km=12.5,
    )

    print("===== Pedido original (agosto) =====")
    print(pedido_agosto)

    pedido_setembro = pedido_agosto.clonar_para_proximo_mes()

    pedido_setembro.cesta.substituir_quantidade("Feijão", 5.0)
    pedido_setembro.cesta.substituir_quantidade("Banana", 6.0)
    pedido_setembro.distancia_entrega_km = 15.0

    print("\n===== Pedido clonado (setembro, com ajustes) =====")
    print(pedido_setembro)

    print("\n===== Pedido original após a clonagem (não deve ter mudado) =====")
    print(pedido_agosto)

    print(f"\npedido_agosto is pedido_setembro ? {pedido_agosto is pedido_setembro}")
    print(f"mesma instância de cesta? {pedido_agosto.cesta is pedido_setembro.cesta}")


if __name__ == "__main__":
    main()
