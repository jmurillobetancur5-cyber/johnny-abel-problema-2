# =========================================================
# Nombre: Jhonny Abel Murillo Beetancur
# Programa: Ingeniería de Sistemas
# Universidad: Universidad Nacional Abierta y a Distancia 
# Fuente: Autoría propia
# =========================================================

# ==========================================
# CONSTANTES / PARÁMETROS CONFIGURABLES
# ==========================================
# Definimos la lógica de negocio como constantes

CATEGORIA_OBJETIVO = "Bebidas"  # Categoría a la que se le aplica la promoción
UMBRAL_PRECIO = 50.0            # Precio base mínimo para aplicar el descuento
DESCUENTO = 0.15                # 15% de descuento

# ==========================================
# DATOS INICIALES (Matriz del Menú)
# ==========================================
# Formato de cada fila: [Nombre del Producto, Categoría, Precio Base]
menu_restaurante = [
    ["Hamburguesa", "Comida", 65.0],    # No es de la categoría objetivo
    ["Refresco Grande", "Bebidas", 55.0], # ¡Aplica! Es Bebida y es mayor a 50
    ["Papas Fritas", "Comida", 30.0],   # No es de la categoría objetivo
    ["Jugo Natural", "Bebidas", 45.0],   # Es Bebida, pero NO supera el umbral de 50
    ["Pizza Personal", "Comida", 80.0], # No es de la categoría objetivo
    ["Cerveza Artesanal", "Bebidas", 70.0] # ¡Aplica! Es Bebida y es mayor a 50
]

# ==========================================
# MÓDULO / FUNCIÓN
# ==========================================
def calcular_precio_final(categoria, precio_base):
    """
    Calcula el precio final aplicando un 15% de descuento si el producto
    es de la categoría objetivo y supera el umbral de precio establecido.
    """
    # Estructura condicional con operador lógico 'and' (debe cumplir AMBAS condiciones)
    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        # Calculamos el precio final restando el 15%
        precio_final = precio_base * (1 - DESCUENTO)
        return precio_final
    else:
        # Si no cumple, se mantiene el precio base original
        return precio_base

# ==========================================
# SALIDA (Estructura Repetitiva)
# ==========================================
print("=========================================================")
print("             MENÚ DEL RESTAURANTE - PROMOCIONES          ")
print(f"   (Promoción: 15% desc. en {CATEGORIA_OBJETIVO} mayores a ${UMBRAL_PRECIO})")
print("=========================================================")
print(f"{'Producto':<20} | {'Categoría':<12} | {'Precio Base':<12} | {'Precio Final':<12}")
print("---------------------------------------------------------")

# Recorremos la matriz producto por producto usando un bucle FOR
for producto in menu_restaurante:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]
    
    # Llamamos a la función para procesar el precio
    precio_final = calcular_precio_final(categoria, precio_base)
    
    # Imprimimos los resultados con formato de dinero (.2f fuerza 2 decimales)
    print(f"{nombre:<20} | {categoria:<12} | ${precio_base:<11.2f} | ${precio_final:<11.2f}")

print("=========================================================")