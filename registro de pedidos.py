import pyttsx3
import random 
engine = pyttsx3.init()
productos_disponibles = {
    "pescado": 15000,
    "cachama": 18000,
    "tilapia": 20000,
    "bagre": 22000
}
engine.say("Bienvenido al registro de pedidos de pesca")
engine.runAndWait()
print("Bienvenido al registro de pedidos de pesca")
print("\nProductos disponibles:")
for producto, precio in productos_disponibles.items():
    print(f"- {producto.capitalize()}: ${precio}")
engine.say("Los productos disponibles son: pescado, cachama, tilapia y bagre")
engine.runAndWait()
engine.say("Ingrese cuántos productos diferentes va a registrar")
engine.runAndWait()
cantidad_productos = int(input("\n¿Cuántos productos diferentes desea registrar?: "))
ventas = {}
for i in range(cantidad_productos):
    producto = input(f"Ingrese el nombre del producto #{i+1}: ").lower()
    if producto in productos_disponibles:
        cantidad = int(input(f"Ingrese la cantidad de unidades vendidas de {producto}: "))
        ventas[producto] = cantidad
        engine.say(f"{cantidad} unidades de {producto} registradas")
    else:
        print(f"'{producto}' no está disponible.")
        engine.say("Producto no disponible, por favor intente de nuevo")
    engine.runAndWait()
total_general = 0
print("\nResumen de ventas del día:")
engine.say("Resumen de ventas del día")
engine.runAndWait()
for producto, cantidad in ventas.items():
    subtotal = cantidad * productos_disponibles[producto]
    total_general += subtotal
    print(f"- {producto.capitalize()}: {cantidad} unidades × ${productos_disponibles[producto]} = ${subtotal}")
    engine.say(f"{cantidad} unidades de {producto}, total {subtotal} pesos")
engine.runAndWait()
print(f"\nTotal del día: ${total_general}")
engine.say(f"El total del día fue {total_general} pesos")
engine.runAndWait()
producto_aleatorio = random.choice(list(productos_disponibles.keys()))
print(f"\nSugerencia del día: {producto_aleatorio.capitalize()} - ${productos_disponibles[producto_aleatorio]}")
engine.say(f"Sugerencia del día: {producto_aleatorio}")
engine.runAndWait()