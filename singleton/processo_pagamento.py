from logger import Logger


class ProcessoPagamento:
    def __init__(self, nome_processo: str):
        self.nome_processo = nome_processo

    def executar(self) -> None:
        logger = Logger.get_instance()
        logger.log(self.nome_processo, "Validando dados de pagamento.")
        logger.log(self.nome_processo, "Pagamento confirmado.")
