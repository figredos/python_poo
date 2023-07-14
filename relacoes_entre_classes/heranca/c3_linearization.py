class Tipo(type):
    def __repr__(cls):
        return cls.__name__


class O(object, metaclass=Tipo):
    pass


# Classes base
class A(O):
    pass


class B(O):
    pass


class C(O):
    pass


class D(O):
    pass


class E(O):
    pass


# Criando árvore de heranças
class K1(C, A, B):
    pass


class K2(B, D, E):
    pass


class K3(A, D):
    pass


class Z(K1, K2, K3):
    pass


# Demonstrando a ordem de resolução de métodos
print(Z.mro())
