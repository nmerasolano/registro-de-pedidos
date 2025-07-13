from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

productos_disponibles = {
    "pescado": 15000,
    "cachama": 18000,
    "tilapia": 20000,
    "bagre": 22000
}

class PedidoApp(App):
    def build(self):
        self.ventas = {}
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.info = Label(text="Productos disponibles:\nPescado, Cachama, Tilapia, Bagre")
        self.layout.add_widget(self.info)

        self.input_producto = TextInput(hint_text="Producto", multiline=False)
        self.layout.add_widget(self.input_producto)

        self.input_cantidad = TextInput(hint_text="Cantidad", multiline=False, input_filter='int')
        self.layout.add_widget(self.input_cantidad)

        self.boton_agregar = Button(text="Agregar pedido")
        self.boton_agregar.bind(on_press=self.agregar_pedido)
        self.layout.add_widget(self.boton_agregar)

        self.resultado = Label(text="")
        self.layout.add_widget(self.resultado)

        return self.layout

    def agregar_pedido(self, instance):
        producto = self.input_producto.text.lower()
        cantidad = self.input_cantidad.text

        if producto in productos_disponibles and cantidad:
            cantidad = int(cantidad)
            subtotal = cantidad * productos_disponibles[producto]
            self.ventas[producto] = self.ventas.get(producto, 0) + cantidad
            self.resultado.text = f"{cantidad} unidades de {producto} registradas.\nSubtotal: ${subtotal:,}"
        else:
            self.resultado.text = "Producto no válido o cantidad vacía"