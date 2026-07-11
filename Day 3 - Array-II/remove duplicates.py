#Creating a program to remove the duplicates from the array 
def remove_duplicates(arr):
    slow=0
    fast=1
    if len(arr) == 0:
          return 0
    while fast < len(arr):
                if arr[fast] != arr[slow]:
                    slow+=1
                    arr[slow]=arr[fast]
                    fast+=1
                elif arr[fast] == arr[slow]:
                    fast+=1
    return slow+1
arr=[1,1,2,2,3,3,4,4]
k=remove_duplicates(arr)
print(arr[:k])

