import re

def tokenize(expression):
    # Definir el patrón de expresión regular para identificar los tokens
    pattern = r'\(|\)|\*|\+|\||[a-zA-Z]+'
    
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

# Ejemplo de uso
expression = "ab(b)* + (a+b)*b(b(a)*)*"
tokens = tokenize(expression)
print("Tokens:", tokens)
