import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class AutomataView:
    """
    AutomataView
    ============
    Esta clase se encargá de generar la
    interfaz gráfica del automata, de manera
    que podrá  visualizar el funcionamiento del
    modelo, y recibir los datos del regex.
    """
    def __init__(self, root, controller):
        """
        Constructor de la clase.
        - `Args:`
            - `root`: Objeto raíz de Tkinter.
            - `controller`: Controlador del proceso automata.
        """
        self.controller = controller
        self.root = root
        self.root.title("Generador de Autómatas")
        self.root.geometry('1000x500') # Dimensiones iniciales de la ventana
        self.root.resizable(width = 0, height = 0) # Inhabilita el resize de la ventana por usuario

        # Crear el campo de entrada para la expresión regular
        self.expression_label = ttk.Label(root, text="Expresión regular:")
        self.expression_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.expression_entry = ttk.Entry(root, width=30)
        self.expression_entry.grid(row=0, column=1, padx=10, pady=5)

        # Crear el botón para generar el autómata determinista
        self.generate_button = ttk.Button(
            root, text="Generar Autómata ", command=self.generate_automaton
        )
        self.generate_button.grid(row=0, column=2, padx=10, pady=5)

       


        # Espacio para mostrar la imagen del autómata
        self.canvas = tk.Canvas(root, width=1000, height=1000)
        self.canvas.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

    def generate_automaton(self):
        expression = self.expression_entry.get()
        image_file = self.controller.generate_automaton(expression)
        self.show_automaton(image_file)

    def show_automaton(self, image_file):
        self.canvas.delete("all")
        image = Image.open(image_file)
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo
