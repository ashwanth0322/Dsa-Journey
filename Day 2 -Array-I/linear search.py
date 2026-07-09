#Solving a problem using linear search 
def target_element(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

t=int(input("Enter the target element :"))
arr=[3,9,12,4,9]
print("The target value is at index ",target_element(arr,t))
