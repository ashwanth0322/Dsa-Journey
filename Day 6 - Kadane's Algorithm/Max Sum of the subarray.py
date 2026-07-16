#Creating a program to return the max sum of the subarray
#Brute Force 
def max_sum(arr):
    maximum=float('-inf')
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum=sum+arr[j]
            maximum=max(maximum,sum)
    return maximum
arr = [-5, -2, -8]
print(max_sum(arr))