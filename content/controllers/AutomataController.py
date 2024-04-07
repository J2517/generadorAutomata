from content.models.AutomataModel import AutomataModel

class AutomataController:
    """
    Automata
    ========
    Esta clase generá la interacción
    del automata, a través de la función
    `generate_automaton` se hace la interacción
    del automata con la expresión recibida.
    """
    def __init__(self):
        """ Constructor de la clase """
        self.model = AutomataModel()

    def generate_automaton(self, expression):
        return self.model.generate_automaton(expression)
