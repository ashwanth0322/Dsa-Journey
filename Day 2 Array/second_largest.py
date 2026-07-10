#Creating a code to find the second largest eleemnt from the array
def second_largest(arr):
    if len(arr) > 1:
        largest=arr[0]
        sec_largest=float('-inf')
        for i in arr[1:]:
            if i > largest:
                sec_largest=largest
                largest=i
            elif i < largest and i > sec_largest:
                sec_largest=i
            elif largest == sec_largest:
                return -1
            elif sec_largest == float('-inf'):
                return -1
        return sec_largest
    else:
        return -1
arr=[2,2,2]
print(second_largest(arr))