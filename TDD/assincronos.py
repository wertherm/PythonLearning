import asyncio

import unittest
from unittest import TestCase

async def funcaoAssincrona():
    print("Início da função assíncrona")

    await asyncio.sleep(2) #Simula uma operação assíncrona
    #Ao chamar uma função assíncrona, é necessário usar a palavra-chave await.
    #Se você esquecer de usar await, o resultado da chamada será None, o que pode causar: ValueError: a coroutine was expected, got None

    print("Fim da função assíncrona")

async def CreateTask():
    asyncio.create_task(funcaoAssincrona())

#Funções que não contêm a palavra-chave async podem chamar funções assíncronas.
#No entanto, quando você chama uma função assíncrona a partir de uma função síncrona (que não possui a palavra-chave async),
#você geralmente precisa esperar pela conclusão da função assíncrona usando asyncio.run() ou asyncio.create_task().
def funcaoSincrona():
    print("Início da função síncrona")
    
    #funcaoAssincrona() #Se colocar 'await' na frente, você receberá este warning do Pylance: "await" allowed only within async function
    #Se não tiver 'await' em modo de execução, ocorrerá:
    #RuntimeWarning: coroutine 'funcaoAssincrona' was never awaited funcaoAssincrona()
    #RuntimeWarning: Enable tracemalloc to get the object allocation traceback
    #Por isso tem que chamar a função assíncrona usando asyncio.run()
    asyncio.run(funcaoAssincrona())
    
    #Ou chamar a função assíncrona usando asyncio.create_task()
    #asyncio.create_task(funcaoAssincrona())
    #Lembre-se que asyncio.run() cria automaticamente e executa um loop de eventos assíncronos para a função fornecida.
    #No entanto, se você chamar asyncio.create_task() diretamente fora de uma função assíncrona ou sem um loop de eventos,
    #você receberá RuntimeError: no running event loop
    #Para resolver isso você pode colocar asyncio.create_task() em outra função e chamá-la com asyncio.run()
    #asyncio.run(CreateTask())
    
    #Lembre-se de que, ao chamar uma função assíncrona a partir de uma função síncrona, você está efetivamente bloqueando
    #a execução da função síncrona até que a função assíncrona seja concluída, a menos que você use técnicas como
    #asyncio.run() ou asyncio.create_task() para evitar esse bloqueio.

    print("Fim da função síncrona")

class TestesAssincronos(TestCase):
    #Testes de assincronicidade
    def test_Assincronos(self):
        funcaoSincrona()

if __name__ == "__main__":
    unittest.main()