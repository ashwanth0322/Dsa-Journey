#Creating a code that returns the next largest permuttation
def permutation(arr):
    pivot=-1
    for i in range(len(arr)-2,-1,-1):
        if arr[i] < arr[i+1]:
            pivot=i
            break
    if pivot == -1:
        left=0
        right=len(arr)-1
        while right > left:
            [arr[left],arr[right]]=[arr[right],arr[left]]
            left+=1
            right-=1
        return arr
    for j in range(len(arr)-1,0,-1):
        if arr[j] > arr[pivot]:
            [arr[pivot],arr[j]]=[arr[j],arr[pivot]]
            break
    left=pivot+1
    right=len(arr)-1
    while right > left:
        [arr[left],arr[right]]=[arr[right],arr[left]]
        left+=1
        right-=1
    
    return arr
arr=[1,2,3]
print(permutation(arr))


   



