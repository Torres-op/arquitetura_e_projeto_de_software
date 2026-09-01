import threading
from datetime import datetime


class Logger:
    _instancia = None

    _lock = threading.Lock()

    ARQUIVO_LOG = "aplicacao.log"

    def __new__(cls):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = super().__new__(cls)
                    print("[Logger] Instância única criada.")
        return cls._instancia

    @classmethod
    def get_instance(cls) -> "Logger":
        """Ponto único de acesso à instância do Logger."""
        return cls()

    def log(self, origem: str, mensagem: str) -> None:
        linha = f"[{datetime.now():%d/%m/%Y %H:%M:%S}] [{origem}] {mensagem}"

        print(linha)

        with self._lock:
            try:
                with open(self.ARQUIVO_LOG, "a", encoding="utf-8") as arquivo:
                    arquivo.write(linha + "\n")
            except OSError as erro:
                print(f"Erro ao gravar log: {erro}")
