items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # se empieza desde el segundo elemento
    j = None

def step():
    global items, n, i, j

    # 1) Si terminamos
    if i >= n:
        return {"done": True}

    # 2) Si j es None: recién vamos a empezar con este i
    if j is None:
        j = i
        return {"a": j, "b": j-1 if j-1 >= 0 else j, "swap": False, "done": False}

    # 3) Si debemos seguir desplazando hacia la izquierda
    #    Mientras j > 0 y items[j-1] > items[j]
    if j > 0 and items[j - 1] > items[j]:
        # swap adyacente (j-1 con j)
        a = j - 1
        b = j
        items[a], items[b] = items[b], items[a]

        j -= 1
        return {"a": a, "b": b, "swap": True, "done": False}

    # 4) Ya no hay que desplazar → avanzar al siguiente i
    i += 1
    j = None

    # Highlight mínimo para mostrar avance
    return {"a": i-1, "b": i-1, "swap": False, "done": False}
