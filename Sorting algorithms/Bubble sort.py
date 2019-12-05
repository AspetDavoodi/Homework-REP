def bubbleSort(Array):
    for num in range(len(Array)-1,0,-1):
        for i in range(num):
            if Array[i]>Array[i+1]:
                temp = Array[i]
                Array[i] = Array[i+1]
                Array[i+1] = temp

Array = [64,25,0,1,2,5,14,55,82,4,2565,21456,25,25,52,624,0]
bubbleSort(Array)
print(Array)
