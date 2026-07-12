#Create a code that moves zeros to the right side of the array
def move_zeros(arr):
    slow=0
    fast=0
    while fast < len(arr):
        if arr[fast] == 0:
            fast+=1
        elif arr[fast] != 0:
            temp=arr[slow]
            arr[slow]=arr[fast]
            arr[fast]=temp
            slow+=1
            fast+=1
    return arr
arr=[1,3,0,0,4]
print(move_zeros(arr))
