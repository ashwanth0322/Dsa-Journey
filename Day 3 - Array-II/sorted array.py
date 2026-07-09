#Creating a program to check whether a given array is sorted or not 
def sorted_array(arr):
    left=0
    right=1
    while right <= len(arr)-1:
        if arr[left] <= arr[right]:
            left+=1
            right+=1
        else:
            return False
    return True
        
        
    
arr=[2,4,6,6,10]
print(sorted_array(arr))