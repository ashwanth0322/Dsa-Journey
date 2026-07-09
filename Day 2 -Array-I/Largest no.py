#Create a program to return the largest number of the array
def largest_element(arr):
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest=arr[i]
    return largest

arr=[12, 7, 25, 4, 18]
print("The largest element in the array :",largest_element(arr))