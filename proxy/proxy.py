from abc import ABC, abstractmethod


class UsuarioInterface(ABC):
    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_cpf(self):
        pass

    @abstractmethod
    def get_endereco(self):
        pass


class Usuario(UsuarioInterface):
    def __init__(self, nome, cpf, endereco):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco

    def get_nome(self):
        return self._nome

    def get_cpf(self):
        return self._cpf

    def get_endereco(self):
        return self._endereco


class UsuarioProxy(UsuarioInterface):
    def __init__(self, usuario: Usuario):
        self._usuario = usuario

    def get_nome(self):
        return self._usuario.get_nome()

    def get_cpf(self):
        cpf = ''.join(filter(str.isdigit, self._usuario.get_cpf()))

        if len(cpf) != 11:
            return "CPF inválido"

        return f"***{cpf[3:9]}**"

    def get_endereco(self):
        raise PermissionError("Acesso ao endereço negado pela LGPD.")


class Principal:
    @staticmethod
    def main():
        usuario = Usuario(
            nome="Ana Silva",
            cpf="123.456.789-01",
            endereco="Rua Principal, 123"
        )

        proxy = UsuarioProxy(usuario)

        print("Nome:", proxy.get_nome())
        print("CPF:", proxy.get_cpf())

        try:
            print("Endereço:", proxy.get_endereco())
        except PermissionError as erro:
            print("Endereço: acesso negado ->", erro)


if __name__ == "__main__":
    Principal.main()