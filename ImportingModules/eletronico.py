class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligado(self):
        if not self._ligado:
            self._ligado = True
            print(f"O {self._nome} esta ligado")

    def desligado(self):
        if self._ligado:
            self._ligado = False
            print(f"O {self._nome} esta desligado")