from typing import List

from gestion_de_ramos.flor import Flor
from gestion_de_ramos.ramo import Ramo


class InventarioFlores:
    flores: List[Flor]
    ramos: List[Ramo]

    def __init__(self):
        self.flores = []
        self.flores.append(Flor(nombre="Rosa", cantidad=5, color="rojo", precio=500))
        self.flores.append(Flor(nombre="Margarita", cantidad=3, color="Blancas", precio=300))
        self.flores.append(Flor(nombre="Tulipan", cantidad=2, color="azul", precio=1200))
        self.flores.append(Flor(nombre="Ave del Paraiso", cantidad=5, color="rojo", precio=1500))
        self.flores.append(Flor(nombre="Rosa", cantidad=5, color="Azul", precio=550))

        self.ramos = []

    def alta(self, numero_flor, cantidad):
        self.flores[numero_flor].cantidad += cantidad

    def baja(self, numero_flor, cantidad):
        self.flores[numero_flor].cantidad -= cantidad

    def vender_ramo(self, numero_ramo):
        self.ramos.pop(numero_ramo)
