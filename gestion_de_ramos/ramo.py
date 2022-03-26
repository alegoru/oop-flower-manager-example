from typing import List

from gestion_de_ramos.flor import Flor


class Ramo:
    flores: List[Flor]

    def __init__(self):
        self.flores = []

    def agregar_flor(self, flor):
        self.flores.append(flor)

    def tamano(self):
        return len(self.flores)

    def precio(self):
        precio = 0
        for flor in self.flores:
            precio += flor.precio
        return precio
