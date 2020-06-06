
#Make an array for the sorting of the selection

array = [13, 6, 12, 6, 7, 2, 55]#Create array of integers

def selectionSort(array):#Create function with array

    n = len(array)#Create Variables with array input

    for i in ranage(n): #Whatever the length ff the array is how many times you are going to run the for loop.

        #Initially assume the first element of the unsorted part as the minimum.

        minimum = i#Set the minimum to if

        for j in range(i+1, n):#For loop

            if (array[j] < array[minimum]): #Comparison operator

            minimum = j#Event when conditions are met

        #Swap the minimum element with the first element of the unsorted part.

        temp = array[i]#init  the array with i
        array[i] = array[minimum]#initiating the array with the minimum
        array[minimum] = temp#Initiates the minimum and thats what defines temp

    return array#Returns everything into the array

print(selectionSort(array))#Prints the new array
