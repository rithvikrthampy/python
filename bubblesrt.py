def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]

arr = []
l1 = int(input("Enter the list size"))

for k in range(0,l1):
    print ("Enter number at index", k)
    item = int(input())
    arr.append(item)

print("Unsorted list: ", arr)

bubbleSort(arr)

print("Sorted list: ", arr)
