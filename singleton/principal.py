from logger import Logger
from processo_pedido import ProcessoPedido
from processo_pagamento import ProcessoPagamento


def main() -> None:
    logger1 = Logger.get_instance()

    pedido1 = ProcessoPedido("Pedido-001")
    pedido2 = ProcessoPedido("Pedido-002")
    pagamento1 = ProcessoPagamento("Pagamento-001")

    pedido1.executar()
    pagamento1.executar()
    pedido2.executar()

    logger2 = Logger.get_instance()
    logger2.log("Principal", "Todos os processos foram concluídos.")

    print()
    print(f"logger1 is logger2 ? {logger1 is logger2}")
    print(f"id(logger1): {id(logger1)}")
    print(f"id(logger2): {id(logger2)}")


if __name__ == "__main__":
    main()
