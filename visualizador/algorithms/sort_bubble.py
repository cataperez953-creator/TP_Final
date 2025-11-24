# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    # TODO: implementamos bubble sort incremental, donde cada llamada a step() hace solo un par de indices.
# 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
# 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
# 3) Avanzar punteros (preparar el próximo pa
# 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.
