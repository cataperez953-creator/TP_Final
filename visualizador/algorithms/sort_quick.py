def quickSort (array, low, high):
    if low < high:
        pivote = partition (array, low, high)
    quickSort (array, low, pivote - 1)
    quickSort (array, pivote + 1, high)

def partition (array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range (low, high):
        if array [j] <= pivot:
            i = i + 1
            (array [i], array [j]) = (array [j], array [i])
    (array [i + 1], array [high]) = (array[high], array[i + 1])
    return i + 1