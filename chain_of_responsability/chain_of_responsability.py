class Conta:
    def __init__(self, saldo, tipo, bloqueio_judicial=False):
        self.saldo = saldo
        self.tipo = tipo
        self.bloqueio_judicial = bloqueio_judicial


class Transacao:
    def __init__(self, conta, valor):
        self.conta = conta
        self.valor = valor


class Handler:
    def __init__(self):
        self._proximo = None

    def set_proximo(self, proximo):
        self._proximo = proximo
        return proximo

    def processar(self, transacao):
        if self._proximo is not None:
            return self._proximo.processar(transacao)

        return True, "Transação autorizada"


class RegraSaldo(Handler):
    def processar(self, transacao):
        if transacao.conta.saldo < transacao.valor:
            return False, "Saldo insuficiente"

        return super().processar(transacao)


class RegraValorMaximo(Handler):
    def processar(self, transacao):
        tipo = transacao.conta.tipo.lower()

        if tipo == "comum":
            limite = 1000.00
        elif tipo == "premium":
            limite = 10000.00
        else:
            return False, "Tipo de conta inválido"

        if transacao.valor > limite:
            return (
                False,
                f"Valor excede o limite de R$ {limite:.2f} para conta {transacao.conta.tipo}"
            )

        return super().processar(transacao)


class RegraBloqueioJudicial(Handler):
    def processar(self, transacao):
        if transacao.conta.bloqueio_judicial:
            return False, "Conta com bloqueio judicial"

        return super().processar(transacao)


class Principal:
    @staticmethod
    def montar_cadeia():
        regra_saldo = RegraSaldo()
        regra_valor_maximo = RegraValorMaximo()
        regra_bloqueio_judicial = RegraBloqueioJudicial()

        regra_saldo.set_proximo(regra_valor_maximo).set_proximo(regra_bloqueio_judicial)

        return regra_saldo

    @staticmethod
    def autorizar(cadeia, descricao, transacao):
        aprovada, motivo = cadeia.processar(transacao)

        status = "AUTORIZADA" if aprovada else "NEGADA"
        print(f"{descricao}: {status} - {motivo}")

        return aprovada

    @staticmethod
    def main():
        cadeia = Principal.montar_cadeia()

        conta_comum = Conta(saldo=1500.00, tipo="Comum")
        conta_comum_bloqueada = Conta(
            saldo=5000.00,
            tipo="Comum",
            bloqueio_judicial=True
        )
        conta_premium = Conta(saldo=20000.00, tipo="Premium")
        conta_premium_saldo_baixo = Conta(saldo=5000.00, tipo="Premium")

        Principal.autorizar(
            cadeia,
            "Comum, R$ 800,00",
            Transacao(conta_comum, 800.00)
        )

        Principal.autorizar(
            cadeia,
            "Comum, R$ 1.200,00",
            Transacao(conta_comum, 1200.00)
        )

        Principal.autorizar(
            cadeia,
            "Premium, R$ 9.000,00",
            Transacao(conta_premium, 9000.00)
        )

        Principal.autorizar(
            cadeia,
            "Premium com saldo baixo, R$ 6.000,00",
            Transacao(conta_premium_saldo_baixo, 6000.00)
        )

        Principal.autorizar(
            cadeia,
            "Comum bloqueada judicialmente, R$ 500,00",
            Transacao(conta_comum_bloqueada, 500.00)
        )


if __name__ == "__main__":
    Principal.main()