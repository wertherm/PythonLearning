#Glossário:
#   module - É qualquer arquivo.py
#   package - É qualquer diretório contendo diversos arquivos.py
#   objeto - Quase tudo é um objeto, funções, classes, variáveis, etc.

#Erro de importação de módulos dentro subdiretórios:
#   Importações absolutas (from pacote.modulo import classe) só funcionam se forem executadas a partir de um arquivo que esteja na raiz do projeto.
#   Ocorrerá erros de importação, se você executar algum módulo dentro subdiretórios da raiz do projeto.

#Testando importação de módulos e pacotes:
#Aponte para o diretório que deve importar algum módulo ou pacote no CLI. Execute o REPL do Python:
#	>>> import modulo
#ou
#	>>> import pacote.modulo
#ou
#	>>> from pacote.modulo import classe
#	>>> dir() #Comando que mostra o dicionário de dados da Tabela de símbolos (variáveis, funções e classes definidas neste módulo). Se fizer um import e ele aparecer nessa lista, então as dependências estarão funcionando.