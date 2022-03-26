class Flor:
    nombre: str
    color: str
    cantidad: int
    precio: float


    def __init__(self,nombre,color,cantidad,precio):
        self.nombre = nombre
        self.color = color
        self.cantidad = cantidad
        self.precio = precio

    def __repr__(self):
        return f"\n{self.nombre=}  {self.color=} {self.cantidad=} {self.precio=}"
