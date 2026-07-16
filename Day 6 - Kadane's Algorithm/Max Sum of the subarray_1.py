#Creating a program that returns the max sum of subarray
#Kadane's Algorithm
#Time Complexity = O(n)
#Extra Space = O(1)
def max_sum(arr):
    current_sum=0
    maximum=float('-inf')
    for i in arr:
        current_sum+=i
        if current_sum < i:
            current_sum=i
        maximum=max(maximum,current_sum)
    return maximum
arr=[2,-1,3]
print(max_sum(arr))
