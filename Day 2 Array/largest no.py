#Create a Code that returns the largest no from the array
def largest_no(arr):
    largest=arr[0]
    for i in arr[1:]:
        if i > largest:
            largest=i
    return largest
arr=[2,4,6,5,1]
print("Largest No :",largest_no(arr))