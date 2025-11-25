# Estado global
items = []
n = 0
i = 0
j = 0
finished = False


def init(vals):
    global items, n, i, j, finished
    items = list(vals)
    n = len(items)
    i = 0
    j = 0
    finished = False


def step():
    global items, n, i, j, finished

    if finished:
        return {"done": True}

    if i >= n - 1:
        finished = True
        return {"done": True}

    a = j
    b = j + 1
    swapped = False

    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swapped = True

    j += 1
    if j >= n - i - 1:
        j = 0
        i += 1

    return {
        "a": a,
        "b": b,
        "swap": swapped,
        "done": False
    }
