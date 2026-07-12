#Create a program that left rotates the array
def rotate_array(arr):
    temp=arr[0] #10

    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=temp
    return arr
arr = [10,20,30,40,50]
print(rotate_array(arr)) 