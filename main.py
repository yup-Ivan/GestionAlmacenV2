from models import (
                    Articulo, 
                    Servicio, 
                    Ubicacion, 
                    Transaccion, 
                    SolicitudPedido,
                    )

if __name__ == '__main__':

    articulo1 = Articulo("A001", "Camiseta de algodón", "Ropa", True, True, True, 0.16, 50, False, "CS001", "L001", 15.99)
    print(articulo1.activo)
    articulo2 = Articulo("A002", "Smartphone", "Electrónica", True, True, True, 0.21, 20, False, "SP001", "L002", 399.99)
    articulo3 = Articulo("A003", "Leche entera", "Alimentos", True, True, True, 0.10, 100, True, "LE001", "L003", 1.99)
    articulo4 = Articulo("A004", "Pelota de fútbol", "Deporte", True, True, True, 0.21, 30, False, "PF001", "L004", 9.99)
    articulo5 = Articulo("A005", "Libro de ciencia ficción", "Libros", True, True, True, 0.04, 10, False, "LF001", "L005", 20.50)

    ubicacion1 = Ubicacion("UB001", "Almacén principal", True)
    ubicacion3 = Ubicacion("UB003", "Estantería A", False)

    maestro_articulos = [articulo1, articulo2, articulo3, articulo4, articulo5]
    maestro_ubicaciones = [ubicacion1, ubicacion3]

    # Stock inicial.
    transaccion1 = Transaccion(articulo1, 100, ubicacion1, ubicacion3)
    transaccion2 = Transaccion(articulo2, 50, ubicacion1, ubicacion3)
    transaccion3 = Transaccion(articulo3, 200, ubicacion1, ubicacion3)
    transaccion4 = Transaccion(articulo4, 80, ubicacion1, ubicacion3)

    # Transferencias entre ubicaciones.
    transacciones = [
        # transaccion1,
        # transaccion2,
        # transaccion3,
        # transaccion4,
        Transaccion(articulo1, 100, ubicacion1, ubicacion3),
        Transaccion(articulo2, 50, ubicacion1, ubicacion3),
        Transaccion(articulo3, 200, ubicacion1, ubicacion3),
        Transaccion(articulo4, 80, ubicacion1, ubicacion3),
        Transaccion(articulo1, 20, ubicacion1, ubicacion3),
        Transaccion(articulo2, 10, ubicacion1, ubicacion3),
        Transaccion(articulo3, 50, ubicacion1, ubicacion3),
        Transaccion(articulo4, 30, ubicacion1, ubicacion3),
        Transaccion(articulo1, 15, ubicacion3, ubicacion1),
        Transaccion(articulo2, 8, ubicacion3, ubicacion1)
    ]

    unidades_por_ubicacion = {}

    for transaccion in transacciones:
        articulo = transaccion.articulo
        ubicacion_destino = transaccion.ubi_destino
        cantidad = transaccion.cantidad

        if ubicacion_destino in unidades_por_ubicacion:
            if articulo in unidades_por_ubicacion[ubicacion_destino]:
                unidades_por_ubicacion[ubicacion_destino][articulo] += cantidad
            else:
                unidades_por_ubicacion[ubicacion_destino][articulo] = cantidad
        else:
            unidades_por_ubicacion[ubicacion_destino] = {articulo: cantidad}

    for ubicacion, unidades_articulos in unidades_por_ubicacion.items():
        print(f"Ubicación: {ubicacion.codigo}")
        for articulo, unidades in unidades_articulos.items():
            print(f"articulo: {articulo}{unidades} unidades")