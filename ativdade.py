#criação da classe
class Carro():

    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def dirigir(self):
        return f"O {self.modelo} da marca {self.marca}, ano {self.ano}, está em movimento."

    def estacionar(self):
        return f"O carro {self.modelo} de cor {self.cor} foi estacionado."

#criação dos objetos
carro1 = Carro("Toyota", "Corolla", 2020, "preto")
carro2 = Carro("Honda", "Civic", 2019, "branco")
carro3 = Carro("Ford", "Focus", 2018, "prata")
carro4 = Carro("Chevrolet", "Onix", 2021, "vermelho")

#imprimir os resultados
print(carro1.dirigir())
print(carro1.estacionar())

print(carro2.dirigir())
print(carro2.estacionar())

print(carro3.dirigir())
print(carro3.estacionar())

print(carro4.dirigir())
print(carro4.estacionar())