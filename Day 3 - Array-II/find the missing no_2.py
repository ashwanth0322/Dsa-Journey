#Creating a program to find the missing number using sum of the n integers formula
def find_missing_no(arr):
    n=len(arr)+1
    expected=n*(n+1)/2
    actual=0
    for i in arr:
        actual+=i
    missing=expected-actual
    return int(missing)
arr=[1,2,3,4]
print(find_missing_no(arr))