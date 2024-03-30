import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import os
import re
from datetime import datetime

class AutomataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Autómatas")

        # Crear el campo de entrada para la expresión regular
        self.expression_label = ttk.Label(root, text="Expresión regular:")
        self.expression_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.expression_entry = ttk.Entry(root, width=30)
        self.expression_entry.grid(row=0, column=1, padx=10, pady=5)

        # Crear el botón para generar el autómata
        self.generate_button = ttk.Button(
            root, text="Generar Autómata", command=self.generate_automaton
        )
        self.generate_button.grid(row=0, column=2, padx=10, pady=5)

        # Espacio para mostrar la imagen del autómata
        self.canvas = tk.Canvas(root, width=1000, height=1000)
        self.canvas.grid(row=1, column=0, columnspan=3, padx=20, pady=10)


    def generate_automaton(self):
    # Obtener la expresión regular ingresada por el usuario
        expression = self.expression_entry.get()

        # Obtener tokens de la expresión regular
        tokens = self.tokenize(expression)

        # Llamar a una función para generar el diagrama DOT del autómata
        dot_file = self.generate_dot_file(tokens)

        # Llamar a Graphviz para renderizar el diagrama y generar la imagen del autómata
        output_file = os.path.splitext(dot_file)[0] + ".png"
        subprocess.run(["dot", "-Tpng", dot_file, "-o", output_file])

        # Mostrar la imagen del autómata en el lienzo
        self.show_automaton(output_file)

        # Guardar la expresión en la "base de datos"
        self.save_expression_to_db(expression)
        
    def tokenize(self, expression):
        # Definir el patrón de expresión regular para identificar los tokens
        pattern = r"\(|\)|\*|\+|\||[a-zA-Z]+"

        # Utilizar la función findall de la biblioteca re para encontrar todos los tokens
        tokens = re.findall(pattern, expression)

        # Separar grupos dentro de paréntesis en tokens individuales
        grouped_tokens = []
        for token in tokens:
            if token.startswith("(") and token.endswith(")"):
                # Si el token comienza y termina con paréntesis, es un grupo
                grouped_tokens.extend([char for char in token])
            else:
                grouped_tokens.append(token)

        return grouped_tokens

    def generate_dot_file(self, tokens):
        # Definir el nombre del archivo DOT
        dot_file = "automaton.dot"

        # Abrir el archivo DOT para escribir
        with open(dot_file, "w", encoding="utf-8") as f:
            # Escribir la cabecera del archivo DOT
            f.write("digraph G {\n")
            f.write("  rankdir=LR;\n")

            # Contador para generar nombres de estados
            state_count = 0

            # Estado inicial
            initial_state = f"q{state_count}"
            f.write(f"  {initial_state} [shape=point];\n")
            f.write("  start -> {};\n".format(initial_state))

            # Estado final
            final_state = f"q{state_count + 1}"
            f.write(f"  {final_state} [shape=doublecircle];\n")

            # Estado actual
            current_state = initial_state

            # Iterar sobre los tokens
            for token in tokens:
                # Generar nombres de estados
                state_count += 1
                next_state = f"q{state_count}"

                # Escribir transición en el archivo DOT
                if token == "(":
                    # Si es un paréntesis izquierdo, no hay transición
                    pass
                elif token == ")":
                    # Si es un paréntesis derecho, volver al estado anterior
                    f.write(f"  {current_state} -> {final_state};\n")
                elif token == "+":
                    # Si es un operador de repetición 1 o más veces, crear una transición del estado actual al siguiente estado
                    f.write(f'  {current_state} -> {next_state} [label="ε"];\n')
                    f.write(f"  {next_state} -> {current_state};\n")
                    current_state = next_state
                elif token == "*":
                    # Si es un operador de repetición 0 o más veces, crear una transición del estado actual al siguiente estado
                    f.write(f'  {current_state} -> {next_state} [label="ε"];\n')
                    f.write(f"  {next_state} -> {current_state};\n")
                elif token == "|":
                    # Si es un operador de alternativa, crear una transición del estado inicial a los siguientes estados
                    f.write(f'  start -> {next_state} [label="ε"];\n')
                    f.write(f"  {current_state} -> {final_state};\n")
                    current_state = next_state
                else:
                    # Si es un carácter, crear una transición del estado actual al siguiente estado con el carácter como etiqueta
                    f.write(f'  {current_state} -> {next_state} [label="{token}"];\n')
                    current_state = next_state

            # Escribir el cierre del archivo DOT
            f.write("}\n")

        return dot_file

    def show_automaton(self, image_file):
        # Limpiar el lienzo antes de mostrar la nueva imagen
        self.canvas.delete("all")

        # Cargar la imagen del autómata y mostrarla en el lienzo
        image = Image.open(image_file)
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def save_expression_to_db(self, expression):
        # Nombre del archivo que simula la base de datos
        db_file = "expressions_db.txt"
        # Obtener el timestamp actual
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Escribir la expresión en el archivo
        with open(db_file, "a", encoding="utf-8") as file:
            file.write(f"{timestamp}: {expression}\n")
    
    # El resto del código de la clase permanece igual

def main():
    root = tk.Tk()
    app = AutomataGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
