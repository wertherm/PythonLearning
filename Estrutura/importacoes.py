#Erro de importação de módulos dentro subdiretórios:
#   Importações absolutas (from pacote.modulo import classe) só funcionam se forem executadas a partir de um arquivo que esteja na raiz do projeto.
#   Ocorrerá erros de importação, se você executar algum módulo dentro subdiretórios da raiz do projeto.

#Até o Python 2.7, para que o conjunto de módulos em um diretório fosse considerado um pacote Python, era necessário que um arquivo denominado __init__.py estivesse no diretório com os demais módulos.
#O arquivo poderia inclusive estar vazio, apenas a sua presença era suficiente.

#Seja no Python 2.7, seja no Python 3.3+, um arquivo __init__.py dentro de um subdiretório será sempre o primeiro a ser executado quando um módulo dentro deste subdiretório for chamado.
#Trata-se de uma posição perfeita para definirmos variáveis globais ao pacote, ou mesmo para definir o acesso a funções nos diversos módulos que constituem o pacote.

#Mas a partir do Python 3.3 não é mais necessário utilizar o __init.__.py para esta finalidade. Devido a um mecanismo denominado “Namespace packages”, o pacote é identificado automaticamente.

#Testando importação de módulos e pacotes:
#Aponte para o diretório que deve importar algum módulo ou pacote no CLI. Execute o REPL do Python:
#	>>> import modulo
#ou
#	>>> import pacote.modulo
#ou
#	>>> from pacote.modulo import classe
#	>>> dir() #Comando que mostra o dicionário de dados da Tabela de símbolos (variáveis, funções e classes definidas neste módulo). Se fizer um import e ele aparecer nessa lista, então as dependências estarão funcionando.