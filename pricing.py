def calcular_precio_electronica(precio, cantidad):
    subtotal = precio * cantidad
    if cantidad > 8:
        descuento = subtotal * 0.15
    elif cantidad > 4:
        descuento = subtotal * 0.10
    else:
        descuento = 0
    impuesto = (subtotal - descuento) * 0.16
    return subtotal - descuento + impuesto


def calcular_precio_ropa(precio, cantidad):
    subtotal = precio * cantidad
    if cantidad > 10:
        descuento = subtotal * 0.15
    elif cantidad > 5:
        descuento = subtotal * 0.10
    else:
        descuento = 0
    impuesto = (subtotal - descuento) * 0.16
    return subtotal - descuento + impuesto


def calcular_precio_alimentos(precio, cantidad):
    subtotal = precio * cantidad
    if cantidad > 20:
        descuento = subtotal * 0.05
    else:
        descuento = 0
    impuesto = (subtotal - descuento) * 0.08
    return subtotal - descuento + impuesto


def calcular_precio_final(precio, cantidad, categoria):
    if categoria == "electronica":
        return calcular_precio_electronica(precio, cantidad)
    elif categoria == "ropa":
        return calcular_precio_ropa(precio, cantidad)
    elif categoria == "alimentos":
        return calcular_precio_alimentos(precio, cantidad)
    else:
        return precio * cantidad
