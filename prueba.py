# import re

# def tokenize(expression):
#     # Definir el patrón de expresión regular para identificar los tokens
#     pattern = r'\(|\)|\*|\+|\||[a-zA-Z]+'
    
#     # Utilizar la función findall de la biblioteca re para encontrar todos los tokens
#     tokens = re.findall(pattern, expression)
    
#     # Separar grupos dentro de paréntesis en tokens individuales
#     grouped_tokens = []
#     for token in tokens:
#         if token.startswith("(") and token.endswith(")"):
#             # Si el token comienza y termina con paréntesis, es un grupo
#             grouped_tokens.extend([char for char in token])
#         else:
#             grouped_tokens.append(token)

        
    
#     return grouped_tokens



# # Ejemplo de uso
# expression = "ab(b)* + (a+b)*b(b(a)*)*"
# tokens = tokenize(expression)
# print("Tokens:", tokens)

import re

def simplify_expression(expression):
    # Eliminar repeticiones y agrupaciones innecesarias
    simplified_expression = re.sub(r'\(([^()]+)\)\*', r'\1', expression)  # Eliminar (x)* -> x
    simplified_expression = re.sub(r'\(([^()]+)\)\+', r'\1', simplified_expression)  # Eliminar (x)+ -> x
    simplified_expression = re.sub(r'\(([^()]+)\)\|', r'\1', simplified_expression)  # Eliminar (x)| -> x
    simplified_expression = re.sub(r'\(([a-zA-Z]+)\)\*', r'\1', simplified_expression)  # Eliminar (a)* -> a
    simplified_expression = re.sub(r'\(([a-zA-Z]+)\)\+', r'\1', simplified_expression)  # Eliminar (a)+ -> a
    simplified_expression = re.sub(r'\(([a-zA-Z]+)\)\|', r'\1', simplified_expression)  # Eliminar (a)| -> a
    
    return simplified_expression

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
    
    # Si hay más de cuatro estados, simplificar la expresión
    state_count = sum(1 for token in grouped_tokens if token.isalpha())
    if state_count > 4:
        simplified_expression = simplify_expression(expression)
        return tokenize(simplified_expression)  # Llamar recursivamente con la expresión simplificada
    
    return grouped_tokens

# Ejemplo de uso
expression = "ab(b)* + (a+b)*b(b(a)*)*"
tokens = tokenize(expression)
print("Tokens:", tokens)
