def selectionSort(Array):
   for slot in range(len(Array)-1,0,-1):
       posOfMax=0
       for location in range(1,slot+1):
           if Array[location]>Array[posOfMax]:
               posOfMax = location

       tmp = Array[slot]
       Array[slot] = Array[posOfMax]
       Array[posOfMax] = tmp

Array = [64,25,0,1,2,5,14,55,82,4,2565,21456,25,25,52,624,0]
selectionSort(Array)
print(Array)
