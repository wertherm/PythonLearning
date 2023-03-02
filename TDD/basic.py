#Principio
#https://realpython.com/python-testing
#https://dev.to/womakerscode/testes-em-python-parte-1-introducao-43ei
#https://docs.python.org/pt-br/3/library/unittest.html

#Avançado
#https://coderbook.com/@marcus/how-to-unit-test-functions-without-return-statements-in-python
#http://pythonclub.com.br/tdd-com-python-e-flask.html

#Frameworks, tools, libraries
#https://github.com/atinfo/awesome-test-automation/blob/master/python-test-automation.md

#Testes transformam a entrada e a saída de dados.
#Testes na camada de apresentação são muito custosos, pois existe um forte acoplamento entre estados e comportamentos.

import unittest

#O correto é executar os testes como um script na CLI, para assim executar todos o casos de testes de uma só vez (suite).
#Pois se implementar como um módulo, terá que instanciar as classes e usar condicionais para cada método, quebrando o príncipio FIRST do TDD.
class TestesBasicos(unittest.TestCase):

    #Cada método é um caso de teste, um conjunto de casos de testes é chamado de suite.
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

#Esta linha não funciona se executar este código como um módulo, instanciando as classes.
if __name__ == "__main__":
    unittest.main() #unittest.main() fornece uma interface de linha de comando para o script de teste.

#Serviços vs. Objetos:
#Serviços não devem possuir objetos, intâncias. Somente injeção de classes e interfaces.
#Assim os serviços tendem a ser mais fáceis de testar e refatorar, devido à separação de dados e comportamento.
#Manter os dados separados facilita o teste de unidade destes serviços. Assim não precisa desenvolver uma tonelada de acoplamento temporal em seus serviços, pois eles geralmente são sem estado.