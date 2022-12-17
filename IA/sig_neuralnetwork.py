#Exemplo de código em Python que implementa uma rede neural simples para classificar frutas como maçãs ou laranjas, com base em características como tamanho e cor:

import numpy as np

def sigmoid(x):
  # Implementação da função sigmóide
  return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
  # Derivada da função sigmóide
  return x * (1 - x)

# Entradas de treinamento
training_inputs = np.array([[0,0], [0,1], [1,0], [1,1]])

# Saídas de treinamento (maçã = 0, laranja = 1)
training_outputs = np.array([[0,1,1,0]]).T

# Semente aleatória para reproduzir os resultados
np.random.seed(1)

# Pesos sinápticos inicializados aleatoriamente com média 0
synaptic_weights = 2 * np.random.random((2, 1)) - 1

print('Pesos sinápticos iniciais:')
print(synaptic_weights)

# Treinamento da rede
for iteration in range(20000):

  # Entrada da camada de entrada
  input_layer = training_inputs

  # Saída da camada escondida
  hidden_layer = sigmoid(np.dot(input_layer, synaptic_weights))

  # Erro da camada de saída
  error = training_outputs - hidden_layer

  # Ajuste dos pesos sinápticos
  adjustments = error * sigmoid_derivative(hidden_layer)
  synaptic_weights += np.dot(input_layer.T, adjustments)

print('Pesos sinápticos ajustados:')
print(synaptic_weights)

# Teste da rede com novas entradas
new_inputs = np.array([1, 1])
output = sigmoid(np.dot(new_inputs, synaptic_weights))

print('Nova saída:')
print(output)

#Neste código, estamos utilizando a função sigmóide como a função de ativação da rede neural. A função sigmóide é uma função que recebe um valor de entrada x e produz uma saída entre 0 e 1, o que é útil para classificação binária (neste caso, frutas que são ou maçãs ou laranjas).
#O código define as entradas de treinamento (que são as características das frutas) e as saídas de treinamento (que são as classificações de maçã ou laranja). Em seguida, os pesos sinápticos são inicializados aleatoriamente.