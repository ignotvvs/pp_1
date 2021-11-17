def bubblesort(array):
    z = 0
    for j in range(len(array)-1):
        for i in range(1,len(array)):
            if array[i-1]> array[i]:
                z = array[i]
                array[i] = array[i-1]
                array[i-1] = z
    return array
numbers = [3,5,7,3,1,6,8,2]
#print(bubblesort(numbers))