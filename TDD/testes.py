import unittest

#O correto é executar os testes como um script na CLI, para assim executar todos o casos de testes de uma só vez (suite).
#Pois se implementar como um módulo, terá que instanciar as classes e usar condicionais para cada método, quebrando o príncipio FIRST do TDD.
class TestesBasicos(unittest.TestCase):

    #Cada método é um caso de teste, um conjunto de casos de testes é chamado de suite.
    #
    #Por padrão, apenas métodos cujos nomes começam com test são executados
    #Comando Padrao:
    #   python testes.py
    #Comando Verbose:
    #   python -m unittest -v testes.py
    #Comando para nomes fora do padrão em métodos:
    #   python -m unittest -v modulo.classe.metodo
    def test_soma(self):
        self.assertEqual(1+2, 2, "Resultado não corresponde!")

#unittest.main() fornece uma interface de linha de comando para o script de teste.
#Esta linha não funciona se executar este código como um módulo, instanciando as classes.
if __name__ == "__main__":
    unittest.main()