# 1. Matriz de artículos: [Código, Nombre, Stock Actual, Stock Mínimo]
articulos = [
    [101, "arroz", 20, 30],
    [102, "azucar", 15, 20],
    [103, "aceite", 10, 25],
    [104, "sal", 50, 40],
    [105, "cafe", 5, 15]
]

# 2. Función para calcular la cantidad a pedir
def calcular_reabastecimiento(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0

# 3. Generación del informe
print("=" * 55)
print("     INFORME DE REABASTECIMIENTO DE INVENTARIO")
print("=" * 55)
print(f"{'Código':<10} {'Artículo':<12} {'Stock Act.':<12} {'Cantidad a Pedir'}")
print("-" * 55)

for articulo in articulos:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]
    
    # Llamado a la función
    pedir = calcular_reabastecimiento(stock_actual, stock_minimo)
    
    # Si requiere reabastecimiento, mostramos la fila
    if pedir > 0:
        print(f"{codigo:<10} {nombre.capitalize():<12} {stock_actual:<12} {pedir}")

print("=" * 55)
