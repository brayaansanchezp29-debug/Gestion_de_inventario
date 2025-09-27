"""
Gestión de Inventario Básico en una Empresa
"""

inventario = []

def registrar_producto():
    """Función para registrar un nuevo producto en el inventario"""
    print("\n REGISTRA EL PRODUCTO ")
    
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("Error: El nombre del producto no puede estar vacío")
            return
        
        # Verificar si el producto ya existe
        for producto in inventario:
            if producto['nombre'].lower() == nombre.lower():
                print(f"Error: El producto '{nombre}' ya existe en el inventario")
                return
        
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa")
            return
            
        precio = float(input("Ingrese el precio unitario: $"))
        if precio < 0:
            print("Error: El precio no puede ser negativo")
            return
        
        # Crear el producto y agregarlo al inventario
        producto = {
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio
        }
        
        inventario.append(producto)
        print(f"Producto '{nombre}' registrado exitosamente")
        
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")

def mostrar_inventario():
    """Función para mostrar todos los productos del inventario"""
    print("\n INVENTARIO ACTUAL ")
    
    if not inventario:
        print("El inventario está vacío")
        return
    
    print("Productos registrados:")
    for i, producto in enumerate(inventario, 1):
        print(f"{i}. {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: ${producto['precio']:,.0f}")

def calcular_valor_total():
    """Función para calcular el valor total del inventario"""
    print("\n VALOR TOTAL DEL INVENTARIO ")
    
    if not inventario:
        print("El inventario está vacío")
        return
    
    valor_total = 0
    print("Detalle por producto:")
    
    for producto in inventario:
        valor_producto = producto['cantidad'] * producto['precio']
        valor_total += valor_producto
        print(f"- {producto['nombre']}: {producto['cantidad']} × ${producto['precio']:,.0f} = ${valor_producto:,.0f}")
    
    print(f"\n VALOR TOTAL DEL INVENTARIO: ${valor_total:,.0f}")

def buscar_producto():
    """Función para buscar un producto específico por nombre"""
    print("\n=== BUSCAR PRODUCTO === ")
    
    if not inventario:
        print("El inventario está vacío")
        return
    
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    
    for producto in inventario:
        if producto['nombre'].lower() == nombre_buscar.lower():
            print(f"\n✓ Producto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio unitario: ${producto['precio']:,.0f}")
            print(f"Valor total: ${producto['cantidad'] * producto['precio']:,.0f}")
            return
    
    print(f" El producto '{nombre_buscar}' no se encuentra en el inventario")

def registrar_venta():
    """Función para registrar una venta y actualizar el inventario"""
    print("\n REGISTRAR VENTA ")
    
    if not inventario:
        print("El inventario está vacío, no se pueden realizar ventas")
        return
    
    try:
        nombre_producto = input("Ingrese el nombre del producto vendido: ").strip()
        
        # Buscar el producto en el inventario
        producto_encontrado = None
        for producto in inventario:
            if producto['nombre'].lower() == nombre_producto.lower():
                producto_encontrado = producto
                break
        
        if not producto_encontrado:
            print(f" El producto '{nombre_producto}' no existe en el inventario")
            return
        
        cantidad_venta = int(input(f"Ingrese la cantidad a vender (disponible: {producto_encontrado['cantidad']}): "))
        
        if cantidad_venta <= 0:
            print("Error: La cantidad debe ser mayor a cero")
            return
        
        if cantidad_venta > producto_encontrado['cantidad']:
            print(f" Stock insuficiente. Solo hay {producto_encontrado['cantidad']} unidades disponibles")
            return
        
        # Realizar la venta
        valor_venta = cantidad_venta * producto_encontrado['precio']
        producto_encontrado['cantidad'] -= cantidad_venta
        
        print(f"\n VENTA REGISTRADA EXITOSAMENTE")
        print(f"Producto: {producto_encontrado['nombre']}")
        print(f"Cantidad vendida: {cantidad_venta}")
        print(f"Valor de la venta: ${valor_venta:,.0f}")
        print(f"Stock restante: {producto_encontrado['cantidad']}")
        
        # Si el stock llega a cero, preguntar si desea eliminar el producto
        if producto_encontrado['cantidad'] == 0:
            respuesta = input("¿Desea eliminar el producto del inventario? (s/n): ").lower()
            if respuesta == 's':
                inventario.remove(producto_encontrado)
                print(f"Producto '{nombre_producto}' eliminado del inventario")
        
    except ValueError:
        print("Error: Por favor ingrese un número válido")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    # Menú de inventario
afirmacion = True
mensaje = '''
___________________________________________
|                                         |
|           MENU DE INVENTARIO            |
|               EMPRESARIAL               |
|_________________________________________|
|                                         |
| 1. Regristar producto                   |
| 2. Mostrar inventario                   |
| 3. Calcular valor total del inventario  |
| 4. Buscar producto                      |
| 5. Registar venta                       |
| 6. salir                                |
|_________________________________________|
'''
while afirmacion:
    print(mensaje)
    
    opt = int(input('seleccione una opción (1-6): '))
    
    if opt == 1:
        print("registrar producto")
        registrar_producto()
    elif opt == 2:
        print("mostrar inventario")
        mostrar_inventario()
    elif opt == 3:
        print("calcular valor total")
        calcular_valor_total()
    elif opt == 4:
        print("buscar producto")
        buscar_producto()
    elif opt == 5:
        print("registrar venta")
        registrar_venta()
    elif opt == 6:
        print("Saliendo del sistema...")
        afirmacion = False
    else:
        print("Opción inválida")
        
    if afirmacion:
        input("\nPresione Enter para continuar...")
        print("\n" * 2)