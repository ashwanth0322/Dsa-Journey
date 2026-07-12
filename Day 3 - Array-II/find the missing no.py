#Creating a code to find the missing no
def find_missing_number(arr):
    expected=1
    index=0
    while index < len(arr):
        if expected == arr[index]:
            expected+=1
            index+=1
        else:
            return expected
    return expected
arr=[1,2,3,4,5]
print(find_missing_number(arr))