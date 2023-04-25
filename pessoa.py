class Pessoa:
    def __init__(self, nome="", idade=0, peso=0.0, altura=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = self.idade + 1

    def engordar(self):
        self.peso = self.peso + 1.0

    def emagrecer(self):
        self.peso = self.peso - 1.0

    def crescer(self):
        if self.idade < 21:
            self.altura = self.altura + 0.5
            print("Altura: {}".format(self.altura))
        else:
            print("Altura: {}".format(self.altura))
