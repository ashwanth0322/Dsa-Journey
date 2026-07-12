#Creating a program to show the maximum concecutive one
def max_concecutive_num(arr):
    count=0
    maximum=0
    for i in arr:
        if i == 1:
            count+=1

        elif i != 1:
            count=0
        
        maximum=max(maximum,count)

    return maximum
arr=[1,1,1,0,1,1]
print(max_concecutive_num(arr))