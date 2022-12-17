#Exemplo de código de uma rede neural simples escrita em Python, que pode ser usada para classificar frutas como maçãs ou laranjas com base em características como tamanho e cor:

import numpy as np

class NeuralNetwork:
  def __init__(self):
    # Inicializamos os pesos aleatoriamente
    self.weights = np.random.rand(2)
    self.bias = np.random.rand(1)

  def sigmoid(self, x):
    # Aplicamos a função sigmóide para obter uma saída entre 0 e 1
    return 1 / (1 + np.exp(-x))

  def predict(self, inputs):
    # Calculamos a saída da rede com base nas entradas e pesos
    z = np.dot(inputs, self.weights) + self.bias
    output = self.sigmoid(z)
    return output

# Criamos uma instância da rede neural
nn = NeuralNetwork()

# Fornecemos algumas entradas de exemplo e pedimos para a rede prever a classe (maçã ou laranja)
inputs = np.array([[120, 0.5], [100, 0.7], [80, 0.9]])
predictions = nn.predict(inputs)
print(predictions)

#Neste exemplo, estamos criando uma classe NeuralNetwork que possui dois pesos e um viés inicializados aleatoriamente. A classe também tem uma função sigmoid que aplica a função sigmóide à entrada e uma função predict que calcula a saída da rede com base nas entradas e pesos.
#Para usar a rede, criamos uma instância da classe e, em seguida, fornecemos algumas entradas de exemplo para a função predict. A função retorna as previsões da rede, que são valores entre 0 e 1. Valores próximos a 0 indicam que a rede acha que a fruta é uma laranja, enquanto valores próximos a 1 indicam que a rede acha que a fruta é uma maçã.
#Espero que isso ajude a entender o funcionamento básico de uma rede neural! No entanto, é importante notar que este é apenas um exemplo simples e que redes neurais podem ser muito mais complexas e ter várias camadas ocultas de neurônios. Além disso, existem muitos outros tipos de algoritmos de aprendizado de máquina que podem ser usados para resolver problemas de classificação.