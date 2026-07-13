#Create a code that returns the indices of the elements whose sum matches the target
def two_sum(arr):
    seen={}
    target=5
    for i in range(len(arr)):
        complementary=target-arr[i]
        if complementary in seen:
            return i,seen[complementary]
        else:
            seen[arr[i]]=i
arr=[3,2,4]
print(two_sum(arr))