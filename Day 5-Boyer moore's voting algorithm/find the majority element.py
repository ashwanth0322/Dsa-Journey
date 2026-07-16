#Creating a code that uses boyes moore's algorithm to find the majority element 
def majority_element(arr):
    candidate=None
    count=0
    for i in arr:
        if count == 0:
            candidate =i
            count+=1
        elif candidate == i:
            count+=1
        else:
            count-=1
    count=0
    for i in arr:
        if candidate == i:
            count+=1
    if count > len(arr)/2:
        return candidate,count
    else:
        return -1
arr=[1,2,2,3,2,1,2,3,2]
print(majority_element(arr))