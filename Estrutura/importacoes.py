#Até o Python 2.7 para que o conjunto de módulos em um diretório fosse considerado um pacote Python (import pacote.modulo), era necessário que um arquivo __init__.py estivesse no diretório com os demais módulos.
#O arquivo poderia inclusive estar vazio, apenas a sua presença era suficiente.

#Seja no Python 2.7, seja no Python 3.3+, um arquivo __init__.py dentro de um subdiretório será sempre o primeiro a ser executado quando um módulo dentro deste subdiretório for chamado.
#Trata-se de uma posição perfeita para definirmos variáveis globais ao pacote, ou mesmo para definir o acesso a funções nos diversos módulos que constituem o pacote.

#Só que no Python 3.3 não é mais necessário utilizar o __init.__.py para esta finalidade. Devido a um mecanismo denominado “Namespace packages”, o pacote é identificado automaticamente.
#É necessário apenas ter um arquivo .py na raiz do projeto, para poder trabalhar com importações absolutas (from pacote.modulo import classe).
#Senão ocorrerão erros de importação, se você executar algum módulo dentro de subdiretórios da raiz do projeto, usando importações absolutas.
#Caso deseje apenas trabalhar com a importação de um módulo de forma simples, o arquivo .py pode ficar tanto na raiz do projeto, como dentro de subdiretórios.

#Acesse o diretório que deverá importar algum módulo ou pacote no CLI e teste no REPL (Read, Evaluate, Print, Loop) do Python:
#➜  CryptoPyBot git:(master) ✗ cd plot
#➜  plot git:(master) ✗ python3
#	>>> import modulo
#ou
#	>>> import pacote.modulo
#ou
#	>>> from pacote.modulo import classe
#	>>> dir() #Comando que mostra o dicionário de dados da Tabela de símbolos (variáveis, funções e classes definidas neste módulo). Se fizer um import e ele aparecer nessa lista, então as dependências estão funcionando.
#ou (Sensitive Case)
#	>>> from Exchange import Exchange
#	>>> ex = Exchange('Binance')
#	>>> ex.nome
#	'Binance'

#Referências:
#https://realpython.com/absolute-vs-relative-python-imports
#https://docs.python.org/3/tutorial/modules.html
#https://packaging.python.org/en/latest/guides/packaging-namespace-packages