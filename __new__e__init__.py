# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe



class A:
    def __new__(cls):
        print("antes de criar a inst")
        instancia = super().__new__(cls)  #instancia == self
        print("depois da instancia")
        instancia.x = 213
        return instancia

    def __init__(self):
        print(self)

    
    def __repr__(self):
        return f'A()'
    

a = A()
print(a.x)
# a = object.__new__(A)
# a.__init__()