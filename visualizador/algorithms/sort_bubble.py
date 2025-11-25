# Estado global
items = [] #lista de lo que vamos a ordenar
n = 0 #longitud de la lista
i = 0 #pasadas completadas
j = 0 #compara items[j] con items[j+1]
finished = False #indica si el algoritmo ha terminado


def init(vals):
    global items, n, i, j, finished
    items = list(vals) #copia de entrada
    n = len(items) #tamaño de la lista
    i = 0
    j = 0
    finished = False


def step():
    global items, n, i, j, finished
#si el algoritmo ha terminado, devolver done True
    if finished:
        return {"done": True}

    if i >= n - 1:
        finished = True
        return {"done": True}

    a = j
    b = j + 1
    swapped = False
#comparar y posiblemente intercambiar
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swapped = True
#avanzar cursores
    j += 1
    if j >= n - i - 1:
        j = 0
        i += 1
#devolver resultado del paso
    return {
        "a": a,
        "b": b,
        "swap": swapped,
        "done": False
    }
