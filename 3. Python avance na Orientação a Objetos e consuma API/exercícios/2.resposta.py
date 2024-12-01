# 1) Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
# 2) No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.

from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass
# 3)Crie uma nova classe chamada Carro que herda da classe Veiculo.
# 4) No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def ligar(self):
        print(f"O carro {self.modelo} está ligado.")


# 5) Em um arquivo chamado main.py, importe a classe Carro.
# 6) No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.

from veiculo import Carro

carro1 = Carro(marca="Ford", modelo="Focus", cor="Preto")
carro2 = Carro(marca="Chevrolet", modelo="Cruze", cor="Prata")
carro3 = Carro(marca="Honda", modelo="Civic", cor="Vermelho")

print(f"Carro 1: {carro1.marca} {carro1.modelo}, Cor: {carro1.cor}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Cor: {carro2.cor}")
print(f"Carro 3: {carro3.marca} {carro3.modelo}, Cor: {carro3.cor}")