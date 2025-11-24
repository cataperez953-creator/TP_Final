# sort_selection.py
# Algoritmo de ordenamiento: SELECTION SORT (versión paso a paso para el visualizador)

items = []
n = 0

# Punteros / estado del algoritmo
i = 0
j = 0
min_idx = 0
fase = "buscar"  # "buscar" = buscando mínimo, "swap" = realizar intercambio


def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)

    # Inicializar punteros
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"


def step():
    global items, n, i, j, min_idx, fase

    # Caso final
    if i >= n - 1:
        return {"done": True}

    # ==========================
    # FASE 1: BÚSQUEDA DEL MÍNIMO
    # ==========================
    if fase == "buscar":

        # Comparar j con min_idx
        if items[j] < items[min_idx]:
            min_idx = j

        # Devolver comparación (a=j, b=min_idx)
        a, b = j, min_idx
        swap = False

        # Avanzar j
        j += 1

        # Si terminó la búsqueda, pasar a swap
        if j >= n:
            fase = "swap"

        return {"a": a, "b": b, "swap": swap, "done": False}

    # ==========================
    # FASE 2: HACER EL SWAP
    # ==========================
    else:  # fase == "swap"

        a, b = i, min_idx

        # Hacer el swap real
        items[a], items[b] = items[b], items[a]

        # Avanzar a la próxima pasada
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"

        return {"a": a, "b": b, "swap": True, "done": False}
