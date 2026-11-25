
# Programa: Control de inventario y reabastecimiento
# Problema 3 - Fase 5

def calcular_reabastecimiento(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0

    return cantidad_pedir


# Matriz con los datos de los artículos
inventario = [
    [101, "Arroz", 5, 20],
    [102, "Aceite", 12, 10],
    [103, "Azucar", 3, 15],
    [104, "Cafe", 8, 8],
    [105, "Leche", 4, 12]
]

print("CONTROL DE INVENTARIO")
print("------------------------------")

# Recorrer los artículos y generar el informe
for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_reabastecimiento(
        stock_actual, stock_minimo
    )

    print("Codigo:", codigo)
    print("Articulo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock minimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)
    print("------------------------------")
