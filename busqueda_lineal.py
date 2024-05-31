def busqueda_lineal(lista, objetivo):
    # Creamos un for para que recorra la lista usando el metodo enumerte para obtener su indice
    for indice, elemento in enumerate(lista):
        # Si se encuenta el elemento, retorna indice
        if(elemento == objetivo):
            return indice
    # Si no se encuenta el elemento, retorna el -1
    return -1

# Se crea la lista de ejemplo con sus respectivos elementos
lista = [2,4,0,50,3,1,2]

# Se guarda el valor a buscar
valor_buscar = 50

# Se envía como parámetro la lista y el valor a buscar
print(busqueda_lineal(lista, valor_buscar))

