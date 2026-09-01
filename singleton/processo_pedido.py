from logger import Logger


class ProcessoPedido:
    def __init__(self, nome_processo: str):
        self.nome_processo = nome_processo

    def executar(self) -> None:
        logger = Logger.get_instance()
        logger.log(self.nome_processo, "Iniciando processamento de pedido.")
        logger.log(self.nome_processo, "Pedido processado com sucesso.")
