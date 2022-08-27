
def ins(array):
    for j in range(1, len(array)):
        key = array[j]

        i = j - 1

        while (i > -1) and array[i] > key:
            array[i + 1] = array[i]
            i = i-1
        array[i + 1] = key
    print(j)


ar = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr = ar
ins(arr)

print(arr)
print("ins")
    




