items = []
n = 0
i = 0
j = 0

def init(vals):
    """Inicializa la lista y resetea el estado del bubble sort paso a paso."""
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0


def step():
    """
    Ejecuta un micro-paso del algoritmo Bubble Sort.
    Cada llamada compara items[j] con items[j+1] y, si corresponde, los intercambia.
    Devuelve:
        - done=True cuando ya no quedan pasos.
        - done=False con info del paso en otros casos.
    """
    global items, n, i, j

    # Si ya se completaron todas las pasadas de Bubble Sort
    if i >= n - 1:
        return {"done": True}

    # Índices actuales a comparar
    a = j
    b = j + 1
    swap = False

    # Comparar e intercambiar
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    # Avanzar j (comparación siguiente)
    j += 1

    # Si j llegó al final de la pasada actual, reiniciar y avanzar i
    if j >= n - i - 1:
        j = 0
        i += 1

    # Devolver el resultado del micro-paso
    return {
        "a": a,
        "b": b,
        "swap": swap,
        "done": False
    }
