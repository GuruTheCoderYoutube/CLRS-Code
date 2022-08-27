def insertionSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while (i >= 0) and array[i] < key:
            array[i+1] = array[i]
            i = i-1
        array[i+1] = key

array = [1, 2, 3, 4, 5, 6, 7]
insertionSort(array)
print(array)