from models import *

if __name__ == '__main__':

    articulo1 = Articulo("A001", "Camiseta de algodón", "Ropa", True, True, True, 0.16, 50, False, "CS001", "L001", 15.99)
    articulo2 = Articulo("A002", "Smartphone", "Electrónica", True, True, True, 0.21, 20, False, "SP001", "L002", 399.99)
    articulo3 = Articulo("A003", "Leche entera", "Alimentos", True, True, True, 0.10, 100, True, "LE001", "L003", 1.99)
    articulo4 = Articulo("A004", "Pelota de fútbol", "Deporte", True, True, True, 0.21, 30, False, "PF001", "L004", 9.99)
    articulo5 = Articulo("A005", "Libro de ciencia ficción", "Libros", True, True, True, 0.04, 10, False, "LF001", "L005", 20.50)

    ubicacion1 = Ubicacion("UB001", "Almacén principal", True)
    ubicacion2 = Ubicacion("UB002", "Estantería A", True)
    ubicacion3 = Ubicacion("UB003", "Estantería B", False)

    maestro_articulos = [articulo1, articulo2, articulo3, articulo4]
    maestro_ubicaciones = [ubicacion1, ubicacion2, ubicacion3]

    # Stock inicial.
    transaccion1 = Transaccion("TI001", "Stock inicial", False, articulo1, 100, ubicacion1, ubicacion2)
    transaccion2 = Transaccion("TI002", "Stock inicial", False, articulo2, 50, ubicacion1, ubicacion2)
    transaccion3 = Transaccion("TI003", "Stock inicial", False, articulo3, 200, ubicacion1, ubicacion2)
    transaccion4 = Transaccion("TI004", "Stock inicial", False, articulo4, 80, ubicacion1, ubicacion2)

    # Transferencias entre ubicaciones.
    transacciones = [
        Transaccion("TI001", "Stock inicial", False, articulo1, 100, ubicacion1, ubicacion2),
        Transaccion("TI002", "Stock inicial", False, articulo2, 50, ubicacion1, ubicacion2),
        Transaccion("TI003", "Stock inicial", False, articulo3, 200, ubicacion1, ubicacion2),
        Transaccion("TI004", "Stock inicial", False, articulo4, 80, ubicacion1, ubicacion2),
        Transaccion("TT001", "Transferencia", False, articulo1, 20, ubicacion2, ubicacion3),
        Transaccion("TT002", "Transferencia", False, articulo2, 10, ubicacion2, ubicacion3),
        Transaccion("TT003", "Transferencia", False, articulo3, 50, ubicacion2, ubicacion3),
        Transaccion("TT004", "Transferencia", False, articulo4, 30, ubicacion2, ubicacion3),
        Transaccion("TT005", "Transferencia", False, articulo1, 15, ubicacion3, ubicacion1),
        Transaccion("TT006", "Transferencia", False, articulo2, 8, ubicacion3, ubicacion1)
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

    # Imprimir la cantidad total de unidades por ubicación.
    for ubicacion, unidades_articulos in unidades_por_ubicacion.items():
        print(f"Ubicación: {ubicacion.codigo}")
        for articulo, unidades in unidades_articulos.items():
            print(f"articulo: {articulo}{unidades} unidades")