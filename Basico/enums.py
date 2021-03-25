import enum

class Dias(enum.Enum):
   Dom = 1
   Seg = 2

class Multiple(enum.Enum):
   T1 = 1, 'Teste 1'
   T2 = 2, 'Teste 2'

print (Dias['Seg'])
print (Dias(1))
print (Multiple.T2.value[1])