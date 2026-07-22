#Creating a program that returns the lenght of the concecutive longest subarray
def longest_subarray(arr):
    length=0
    seen=set(arr)
    for i in arr:
        current_length=0
        current_element=i
        if current_element-1 not in seen:
            current_length+=1
        while current_element+1 in seen:
           
            current_length+=1
            current_element+=1


            length=max(length,current_length)
    return length
arr=[100,4,200,3,2,1]
print(longest_subarray(arr))