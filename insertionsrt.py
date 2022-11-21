def insertionSort(arr):
    for i in range(0, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1


arr = []
l1 = int(input("enter the size of the list"))
for k in range(0,l1):
    print("Input the numbers in index", k)
    item = int(input())
    arr.append(item)

print("Unsorted list: ", arr) 
insertionSort(arr)
print("Sorted list", arr)
