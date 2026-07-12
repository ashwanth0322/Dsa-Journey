#Create a code that finds the missing no using Xor
def missing_no(arr):
    xor_1=0
    xor_2=0
    for i in range(1,len(arr)+2):
        xor_1 ^=i
    for i in arr:
        xor_2 ^=i
    return xor_1^xor_2
arr=[5,2,1,3]
print(missing_no(arr))