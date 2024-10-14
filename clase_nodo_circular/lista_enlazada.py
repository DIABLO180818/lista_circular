# lista_enlazada.py

from nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar_final(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def eliminar_multiplos_de_2(self):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor % 2 == 0:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
            else:
                anterior = actual
            actual = actual.siguiente


class ListaCaracteres:
    def __init__(self):
        self.cabeza = None

    def agregar_final(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def encontrar_mayor(self):
        if not self.cabeza:
            return None
        actual = self.cabeza
        mayor = actual.valor
        while actual:
            if actual.valor > mayor:
                mayor = actual.valor
            actual = actual.siguiente
        return mayor

    def a_lista(self):
        actual = self.cabeza
        lista = []
        while actual:
            lista.append(actual.valor)
            actual = actual.siguiente
        return lista
