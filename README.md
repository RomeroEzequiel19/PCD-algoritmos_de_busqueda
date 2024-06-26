# Algoritmos de búsqueda
## Búsqueda Lineal y Búsqueda Binaria

### Búsqueda Lineal

- La búsqueda lineal, también conocida como búsqueda secuencial, es el algoritmo de búsqueda más simple. Se recorre cada elemento de la lista uno por uno hasta encontrar el objetivo o hasta llegar al final de la lista.
- No requiere que la lista esté ordenada. Puede aplicarse a cualquier tipo de secuencia (listas, tuplas, etc.).

Funcionamiento:

1. Comienza en el primer elemento de la lista.
2. Compara cada elemento con el objetivo.
3. Si encuentra el objetivo, retorna el índice del elemento.
4. Si llega al final de la lista sin encontrar el objetivo, retorna -1.

#### Eficiencia del algoritmo

- Tiempo de ejecución

1. En el peor de los casos, el algoritmo tiene que revisar cada elemento de la lista una vez, lo que significa que el tiempo de ejecución es lineal respecto al número de elementos n.
2. Si el objetivo está en el primer elemento de la lista, el algoritmo lo encuentra inmediatamente.
3. En promedio, la búsqueda lineal tendrá que revisar aproximadamente la mitad de los elementos antes de encontrar el objetivo.

- Recursos utilizados

1. Solo necesita espacio adicional constante para variables temporales.

### Búsqueda Binaria

- La búsqueda binaria es un algoritmo de búsqueda mucho más eficiente que la búsqueda lineal, pero solo puede aplicarse a listas ordenadas. Divide la lista en dos partes y descarta la mitad en cada paso, lo que reduce el número de comparaciones significativamente.

Funcionamiento:

1. Inicializa dos índices: inicio y final al principio y al final de la lista, respectivamente.
2. Calcula el índice medio.
3. Compara el elemento en el índice medio con el objetivo.
- Si el elemento es igual al objetivo, retorna el índice.
- Si el elemento es menor que el objetivo, ajusta el índice inicio a medio + 1.
- Si el elemento es mayor que el objetivo, ajusta el índice final a medio - 1.
4. Repite el proceso hasta que inicio sea mayor que final.
5. Si no encuentra el objetivo, retorna -1.

#### Eficiencia del algoritmo

- Tiempo de ejecución

1. En el peor de los casos, el algoritmo reduce el espacio de búsqueda a la mitad en cada paso, lo que significa que el tiempo de ejecución es logarítmico respecto al número de elementos n.
2. Si el objetivo está en el medio de la lista, el algoritmo lo encuentra inmediatamente.
3. En promedio, el tiempo de búsqueda sigue siendo logarítmico debido a la reducción sistemática del espacio de búsqueda.

- Recursos Utilizados

1. Solo necesita espacio adicional constante para variables temporales.

