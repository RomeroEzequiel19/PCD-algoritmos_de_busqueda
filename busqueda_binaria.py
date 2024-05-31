def busqueda_binaria(lista, objetivo):

    # Se inicializan ambos expremos de la lista
    inicio = 0
    final = len(lista) - 1

    # Ejecuta mientras inicio sea menor o igual que el final de la lista
    while (inicio <= final):

        # Se calcula el índice del medio
        medio = (inicio + final) // 2

        # Se verifica si el valor en el índice medio es menor que el objetivo
        if lista[medio] < objetivo:
            # Se ajusta el índice inferior
            inicio = medio + 1
        # Se verifica si el valor en el índice medio es mayor que el objetivo
        elif lista[medio] > objetivo:
            # Se ajusta el índice superior
            final = medio - 1
        #  Se verifica si el valor del indice del medio es el objetivo
        else:
            # Si es igual, lo retorna
            return medio 
    # Si se sale del bucle, el valor no está presente en la lista
    return "El valor no está presente en la lista"

# Se crea la lista de ejemplo con sus respectivos elementos
lista = [0, 2, 3, 4, 9, 50, 70]

# Se guarda el valor a buscar
valor_buscar = 4

# Se envía como parámetro la lista y el valor a buscar
print(busqueda_binaria(lista, valor_buscar))
