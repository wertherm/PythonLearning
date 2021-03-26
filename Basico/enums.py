import enum

class Dias(enum.Enum):
   Dom = 1
   Seg = 2

class EnumMultidimensional(enum.Enum):
   T1 = 1, 'Teste 1'
   T2 = 2, 'Teste 2'

class EnumExtendido(enum.Enum):
    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value

class Nacionalidade(EnumExtendido):
    BR = 0, 'Brasileiro'
    US = 1, 'Americano'
    FR = 2, 'Frances'

print (Dias['Seg'])
print (Dias(1))
print (EnumMultidimensional.T2.value[1])

print()

membro = Dias.Dom
print(membro.name)
print(membro.value)

print()

print(Nacionalidade.BR)
print(int(Nacionalidade.US))
print(Nacionalidade.FR.fullname)
print(Nacionalidade(1))
print(Nacionalidade(2).fullname)