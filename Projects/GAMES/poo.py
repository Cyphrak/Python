# Programação Orientada à Objetos
# Classes e Objetos

class Veiculo:
    def movimentar(self):
        print(f'Sou um veículo e me descolo.')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    # Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro

    # Getter
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')    

    def get_num_registro(self):
        return self.__num_registro

# Herança
class Carro(Veiculo):
    def movimentar(self):
        print(f'Sou um carro e ando pela rua')

class Motocicleta(Veiculo):
    def movimentar(self):
        print('Ando em duas rodas')   

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante,modelo)   

    def get_categoria(self):
        return self.__cat             
 
    def movimentar(self):
        print(f'Eu voo pelo céu')

if __name__=='__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('4965453-1')
    print(f'Registro: {meu_veiculo.get_num_registro()}\n')

    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()

    moto = Motocicleta('Harleu-Davidson', 'Nightster Special')
    moto.movimentar()
    moto.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria: {meu_aviao.get_categoria()}')
