#Creating a code that finds both the min and max in single traversal this uses double learder method
def min_max(arr):
    largest=arr[0]
    smallest=arr[0]
    for i in arr[1:]:
        if i > largest:
            largest=i
        elif i < smallest:
            smallest=i
    return largest,smallest
arr=[2,3,6,4,10,5]
print(min_max(arr))

