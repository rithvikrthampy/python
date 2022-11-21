def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        cur_min_ind = i
        for j in range(i+1, len(arr)):
            if arr[j] <arr[cur_min_ind]:
                cur_min_ind = j

        arr[i], arr[cur_min_ind] = arr[cur_min_ind], arr[i]


arr = []
l1 = int(input("Enter the size of the list"))

for k in range(0,l1):
    print("enter the numbers on the list on index: ", k)
    item = int(input())
    arr.append(item)

print("Unordered list", arr)
selectionSort(arr)
print("Ordered list", arr)