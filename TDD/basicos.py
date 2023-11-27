#Principio
#https://realpython.com/python-testing
#https://dev.to/womakerscode/testes-em-python-parte-1-introducao-43ei
#https://docs.python.org/pt-br/3/library/unittest.html

#Avançado
#https://coderbook.com/@marcus/how-to-unit-test-functions-without-return-statements-in-python
#http://pythonclub.com.br/tdd-com-python-e-flask.html

#Frameworks, tools, libraries
#https://github.com/atinfo/awesome-test-automation/blob/master/python-test-automation.md

#Observações:
#Testes transformam a entrada e a saída de dados.
#Testes na camada de apresentação são muito custosos, pois existe um forte acoplamento entre estados e comportamentos.

import unittest
from unittest.mock import Mock, patch

def funcaoA(x, y):
    return x+y

def funcaoB(x, y):
    return x-y

def funcaoC(x, y):
    return x*y

def funcaoPrincipal():
    resultadoA = funcaoA(1, 2)
    resultadoB = funcaoB(3, 4)
    resultadoC = funcaoC(5, 6)

    return resultadoA, resultadoB, resultadoC

def funcaoCalculo(flag, x, y):
    if flag:
        resultado = x + y
    else:
        resultado = x - y
    return resultado

#Looping com um contador de 1 a 10 onde a cada interação chama a funcaoCalculo().
#Passando o argumento flag = True quando cada item do contador for par e False quando for ímpar.
def funcaoRealizarCalculo():
    for i in range(1, 11):
        resultado = funcaoCalculo(i % 2 == 0, i, i+1)
        print(f"Para i = {i}, resultado = {resultado}")

#O correto é executar os testes como um script na CLI, para assim executar todos o casos de testes de uma só vez (suite).
#Pois se implementar como um módulo, terá que instanciar as classes e usar condicionais para cada método, quebrando o príncipio FIRST do TDD.
class TestesBasicos(unittest.TestCase):
    #Cada função é um caso de teste, um conjunto de casos de testes é chamado de suite.
    #Idependentemente de quantos casos de teste gerarem erros na sua suite, todos serão testados.
    #
    #Apenas funções cujos nomes começam com 'test' serão testadas, assim você pode implementar funções que isolam lógicas
    #que não serão testadas diretamente. Elas devem ficar acima da class TestesBasicos(TestCase).
    #E se por algum acaso as funções tiverem a mesma assinatura, só será realizado um teste apenas.
    #
    #Comando Padrao:
    #   python basic.py
    #Comando Verboso:
    #   python -m unittest -v basic.py
    #Comando para nomes fora do padrão em métodos:
    #   python -m unittest -v modulo.classe.metodo
    def test_soma(self): #Por padrão, apenas métodos cujos nomes começam com test são executados
        #assert 1 + 2 == 2, "Resultado não corresponde!" #Comando built-in (nativo) do Python
        self.assertEqual(1+2, 3, "Resultado não corresponde!")
    
    #Teste para mockear funções externas dentro de uma função principal.
    #Para cada atributo e propriedade de um objeto mockado que é chamado, é criado outro objeto mock vazio,
    #isso facilita para não ocorrer erros, ao chamar atributos e funções não definidas.
    #E para você definir só aquilo que precisa testar.
    #https://realpython.com/python-mock-library
    @patch('__main__.funcaoB')
    @patch('__main__.funcaoA')
    def test_funcao_principal(self, mock_funcaoA, mock_funcaoB):
        mock_resultadoA = Mock()
        mock_resultadoB = Mock()

        #Faz com que o objeto mockado mantenha o estado das propriedades passadas dentro deste teste.
        mock_funcaoA.return_value = mock_resultadoA
        mock_funcaoB.return_value = mock_resultadoB

        #resultadoA, resultadoB já são retornado mockados
        resultadoA, resultadoB, resultadoC = funcaoPrincipal()

        # Verificar se as funções mockadas foram chamadas
        mock_funcaoA.assert_called_once()
        mock_funcaoB.assert_called_once()

        # Verificar se os resultados são os mocks que você configurou
        self.assertEqual(resultadoA, mock_resultadoA)
        self.assertEqual(resultadoB, mock_resultadoB)

        # Verificar se a funcaoC foi chamada normalmente (sem mock)
        self.assertNotEqual(resultadoC, mock_resultadoA)

    @patch('__main__.funcaoCalculo')
    def test_funcaoRealizarCalculo(self, mock_funcaoCalculo):
        #Em um contexto de teste, você pode usar side_effect para simular diferentes comportamentos da
        #função mockada em diferentes chamadas. Por exemplo, você pode configurar side_effect para retornar
        #diferentes valores em chamadas consecutivas ou para lançar exceções em determinadas condições.
        #Esta forma permite que você configure o side_effect posteriormente, depois que o mock já foi criado.
        mock_funcaoCalculo.side_effect = [-1, 5, -1, 9, -1, 13, -1, 17, -1, 21] #Resultados corretos mockados
        #mock_funcaoCalculo.side_effect = [4, 7, 2, 11, 6, 15, 8, 19, 10, 23] #Resultados incorretos mockados
        #Ambas as formas de configurar side_effect são equivalentes e produzirão o mesmo resultado.
        #A escolha entre elas geralmente se resume à preferência de estilo ou ao contexto em que estão sendo usadas.
        #Esta forma permite que você configure o side_effect no momento da criação do mock.
        #mock_funcaoCalculo = Mock(side_effect=[-1, 5, -1, 9, -1, 13, -1, 17, -1, 21])
        #mock_funcaoCalculo = Mock(side_effect=[4, 7, 2, 11, 6, 15, 8, 19, 10, 23])

        funcaoRealizarCalculo()

        #Verificar se a função foi chamada corretamente (dados corretos)
        chamadas_esperadas = [((False, 1, 2),), ((True, 2, 3),), ((False, 3, 4),), ((True, 4, 5),),
                               ((False, 5, 6),), ((True, 6, 7),), ((False, 7, 8),), ((True, 8, 9),),
                               ((False, 9, 10),), ((True, 10, 11),)]
        #Verificar se a função foi chamada incorretamente (dados incorretos)
        # chamadas_esperadas = [((True, 1, 2),), ((False, 2, 3),), ((True, 3, 4),), ((False, 4, 5),),
        #                        ((True, 5, 6),), ((False, 6, 7),), ((True, 7, 8),), ((False, 8, 9),),
        #                        ((True, 9, 10),), ((False, 10, 11),)]
        
        mock_funcaoCalculo.assert_has_calls(chamadas_esperadas)

if __name__ == "__main__": #Esta linha não funciona se executar este código como um módulo, instanciando as classes.
    unittest.main() #unittest.main() fornece uma interface de linha de comando para o script de teste.