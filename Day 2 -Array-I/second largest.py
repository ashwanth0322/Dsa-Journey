#Create a program to return the second largest element of the array 

# Time Complexity = O(n)

# Space Complexity = O(1)

def second_largest(arr):
    if len(arr) > 1:
        if arr[0] > arr[1]:
            largest=arr[0]
            second_largest=arr[1]
        
        else:
            largest=arr[1]
            second_largest=arr[0]
        
        for i in arr:
                if i > largest:
                    second_largest=largest
                    largest=i
                    
                elif i < largest and i > second_largest:
                    second_largest=i 
        return second_largest
    else:
        print("The array have only one element")
arr=[10,2,8,12,11]
print("The Second Largest element in the array :",second_largest(arr))