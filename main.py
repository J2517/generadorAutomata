from tkinter import Tk
from content.controllers.AutomataController import AutomataController
from content.views.AutomataView import AutomataView

def main():
    """
    Metodo de llamado de funciones
    que hacen parte de la compilación
    del automata, a través de la vista
    de Tk del modulo Tkinter.
    """
    ventana = Tk() # Declaración de la ventana de Tkinter
    automata = AutomataController() #  Inicialización del controlador del automata
    AutomataView(ventana, automata) #  Creación de la vista con los elementos gráficos del automata.
    ventana.mainloop() # Metodo para persistencia de la ventana.

if __name__ == "__main__":
    main()
