# Actividad 9

precio_limit = int(input("Dime un precio y te enseño los productos que valen menos: "))

productos = {
    "Camiseta": 15,
    "Pantalón": 25,
    "Zapatos": 30,
    "Gorra": 10,
    "Cinturón": 20,
}

for producto, precio in productos.items():
    if precio < precio_limit:
       print(f"{producto}: {precio}€")
