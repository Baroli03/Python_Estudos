# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class


# class MinhaString(str):
#     def upper(self):
#         print("Chamou upper")
#         retorno = super().upper()
#         print('Depois do upper')
#         return retorno


# string = MinhaString('Luiz')

# print(string.upper())


class A:

    atributo_a = 'Valor a'

    def metodo(self):
        print('A')

class B(A):

    atributo_b = 'Valor b'

    def metodo(self):
        print('B')

class C(B):

    atributo_c = 'Valor c'

    def metodo(self):
        super().metodo()
        print('C')


c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()