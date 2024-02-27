from abc import ABC, abstractmethod

class Publicado:

    def __init__(self, publicado=False):
        self.publicado = publicado

class Activo:

    def __init__(self, activo=True):
        self.activo = activo

class Producto(Publicado, Activo, ABC):

    id = 0

    def __init__(self, codigo : str, descripcion : str, comparable : str, vendible : bool, activo : bool, publicado : bool, iva : float):
        super().__init__(self)
        Publicado.__init__(self, publicado)
        Activo.__init__(self, activo)
        self.id = Producto.id
        Producto.id += 1
        self.codigo = codigo
        self.descripcion = descripcion
        self.comparable = comparable
        self.vendible = vendible
        self.iva = iva

class Articulo(Producto):

    def __init__(self, codigo: str, descripcion: str, comparable: str, vendible: bool, activo: bool, publicado: bool, iva: float, stock_minimo : int, perecedero : bool, num_serie : str, num_lote : str, precio_venta : float):
        super().__init__(codigo, descripcion, comparable, vendible, activo, publicado, iva)
        self.stock_minimo = stock_minimo
        self.perecedero = perecedero
        self.num_serie = num_serie
        self.num_lote = num_lote
        self.precio_venta = precio_venta

    def __str__(self):
        return f'{self.codigo} - {self.descripcion[:50]}'

class Servicio(Producto):

    def __init__(self, codigo: str, descripcion: str, comparable: str, vendible: bool, activo: bool, publicado: bool, iva: float, tipo_servicio : str):
        super().__init__(codigo, descripcion, comparable, vendible, activo, publicado, iva)
        self.tipo_servicio = tipo_servicio

class Ubicacion:

    id = 0

    def __init__(self, codigo : str, descripcion : str, recepcion : bool):
        self.id = Producto.id
        Producto.id += 1
        self.codigo = codigo
        self.descripcion = descripcion
        self.recepcion = recepcion

    def __str__(self):
        return f'{self.codigo} - {self.descripcion[:50]}'

class Transaccion:

    id = 0

    def __init__(self, articulo : Articulo, cantidad : int, ubi_origen : Ubicacion, ubi_destino : Ubicacion):
        self.id = Transaccion.id
        Transaccion.id += 1
        self.articulo = articulo
        self.cantidad = cantidad
        self.ubi_origen = ubi_origen
        self.ubi_destino = ubi_destino

    def __str__(self):
        return f'{self.ubi_origen.codigo} --> {self.ubi_destino.codigo} : {self.articulo.codigo}'

class SolicitudPedido:

    id = 0

    def __init__(self, articulo : Articulo, cantidad : int):
        self.id = SolicitudPedido.id
        SolicitudPedido.id += 1
        self.articulo = articulo
        self.cantidad = cantidad

    def __str__(self):
        return f'{self.articulo.codigo} : {self.cantidad}'