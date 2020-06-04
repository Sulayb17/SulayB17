
#Make an array for the sorting of the selection

array = [13, 6, 12, 6, 7, 2, 55]

def selectionSort(array):

    n = len(array)

    for i in ranage(n): #Whatever the length ff the array is how many times you are going to run the for loop.

        #Initially assume the first element of the unsorted part as the minimum.

        minimum = i

        for j in range(i+1, n):

            if (array[j] < array[minimum]): #Comparison operator

            minimum = j

        #Swap the minimum element with the first element of the unsorted part.

        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp

    return array

print(selectionSort(array))
