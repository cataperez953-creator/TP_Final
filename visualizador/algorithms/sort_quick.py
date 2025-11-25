# Algoritmo de ordenamiento QuickSort:
items = []
n = 0
# Los punteros/estado:
puntero_i = 0      # Índice para el rastreo del último elemento <= pivote
puntero_j = 0      # Puntero que recorre el sub-array (elemento actual a comparar)
indice_pivote = 0  # Índice del elemento pivote (generalmente el final del rango)
limite_inferior = 0# Límite bajo (low) del sub-array actual
limite_superior = 0# Límite alto (high) del sub-array actual
fase_actual = "INIT" # Controla la máquina de estados: "INIT", "PARTICION", "INTERCAMBIO_PIVOTE", "TERMINADO"
pila_rangos = []     # Pila para almacenar los límites (low, high) de los sub-arrays pendientes

def init(vals):
    """Inicializa la lista y el estado del algoritmo."""
    global items, n, puntero_i, puntero_j, indice_pivote, limite_inferior, limite_superior, fase_actual, pila_rangos
    items = list(vals)
    n = len(items)
    
    # Inicialización de punteros/estado
    puntero_i = 0
    puntero_j = 0
    indice_pivote = 0
    limite_inferior = 0
    limite_superior = n - 1
    fase_actual = "INIT"
    pila_rangos = []
    
    if n > 0:
        # Agrega el rango inicial a la pila para comenzar
        pila_rangos.append((limite_inferior, limite_superior))

def _configurar_particion():
    """Configura el estado para el inicio de una partición."""
    global puntero_i, puntero_j, indice_pivote, limite_inferior, limite_superior, fase_actual
    # El pivote es el último elemento del rango
    indice_pivote = limite_superior
    # El puntero i se inicializa justo antes del inicio del rango
    puntero_i = limite_inferior - 1 
    # El puntero j comienza en el primer elemento del rango
    puntero_j = limite_inferior
    fase_actual = "PARTICION"

def step():
    """Implementa UN micro-paso del Quicksort iterativo y devuelve el dict."""
    global items, n, puntero_i, puntero_j, indice_pivote, limite_inferior, limite_superior, fase_actual, pila_rangos

    if fase_actual == "TERMINADO":
        return {"done": True}

    if fase_actual == "INIT":
        if not pila_rangos:
            fase_actual = "TERMINADO"
            return {"done": True}
        
        # Saca un rango de la pila y lo configura
        limite_inferior, limite_superior = pila_rangos.pop()
        
        # Si el sub-array tiene 1 o 0 elementos, avanza al siguiente
        if limite_inferior >= limite_superior:
            return step()
        
        _configurar_particion()

    if fase_actual == "PARTICION":
        # Recorrido de puntero_j
        if puntero_j < indice_pivote:
            # Compara el elemento actual con el pivote
            if items[puntero_j] <= items[indice_pivote]:
                # Si es menor o igual, incrementa i y prepara el posible intercambio con j
                puntero_i += 1
                if puntero_i != puntero_j:
                    # Devuelve el paso de intercambio y pasa a la fase de transición
                    fase_actual = "TRANSICION_SWAP" 
                    return {"a": puntero_i, "b": puntero_j, "swap": True, "done": False}
            
            # Avanza puntero_j para el siguiente elemento
            puntero_j += 1
            # Devuelve el paso de comparación (sin swap)
            indice_a = puntero_i if puntero_i != puntero_j else puntero_j - 1
            return {"a": indice_a, "b": puntero_j - 1, "swap": False, "done": False}

        # Si puntero_j ha llegado al pivote
        elif puntero_j == indice_pivote:
            # Prepara el intercambio final del pivote a su posición correcta (puntero_i + 1)
            puntero_i += 1
            fase_actual = "INTERCAMBIO_PIVOTE"
            return {"a": puntero_i, "b": indice_pivote, "swap": True, "done": False}

    if fase_actual == "TRANSICION_SWAP":
        # Después de que se realiza el swap entre i y j, avanzamos j y volvemos a la PARTICION
        puntero_j += 1 # Ya se avanzó en la llamada anterior, pero por la estructura lo hacemos aquí (o en PARTITION). Lo quitamos de la anterior.
        fase_actual = "PARTICION"
        # Llamamos a step para avanzar la lógica inmediatamente
        return step()
    
    if fase_actual == "INTERCAMBIO_PIVOTE":
        # El pivote ha sido colocado en su posición final: items[puntero_i]
        indice_pivote_final = puntero_i
        
        # 1. Agrega el sub-array izquierdo a la pila 
        if indice_pivote_final - 1 > limite_inferior:
            pila_rangos.append((limite_inferior, indice_pivote_final - 1))
            
        # 2. Agrega el sub-array derecho a la pila
        if indice_pivote_final + 1 < limite_superior:
            pila_rangos.append((indice_pivote_final + 1, limite_superior))

        # Pasamos a la siguiente partición
        fase_actual = "INIT"
        # Devolvemos el estado del pivote finalizado (sin swap en este paso)
        return {"a": indice_pivote_final, "b": indice_pivote_final, "swap": False, "done": False}

    return {"done": False} # Estado por defecto