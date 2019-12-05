def quickSort(alist):
   quickSortguide(alist,0,len(alist)-1)

def quickSortguide(arr,first,last):
   if first<last:

       splitpoint = partition(arr,first,last)

       quickSortguide(arr,first,splitpoint-1)
       quickSortguide(arr,splitpoint+1,last)


def partition(arr,first,last):
   pivot = arr[first]

   left = first+1
   right = last

   done = False
   while not done:

       while left <= right and arr[left] <= pivot:
           left = left + 1

       while arr[right] >= pivot and right >= left:
           right = right -1

       if right < left:
           done = True
       else:
           temp = arr[left]
           arr[left] = arr[right]
           arr[right] = temp

   temp = arr[first]
   arr[first] = arr[right]
   arr[right] = temp


   return right

Array = [64,25,0,1,2,5,14,55,82,4,2565,21456,25,25,52,624,0]
quickSort(Array)
print(Array)