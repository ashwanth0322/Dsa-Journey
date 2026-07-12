#Create a program that rotates the array d plcaes 
def rotate_array(arr):
    temp=[]
    d=int(input("Enter no of elements you want to shift :"))
    for i in range(d):
        temp.append(arr[i])
    for i in range(len(arr)-d):
        arr[i]=arr[i+d]
    for i in range(len(temp)):
        arr[len(arr) - d + i] = temp[i]
   
    return arr
arr=[1,2,3,4,5,6,7]
print(rotate_array(arr))
   

