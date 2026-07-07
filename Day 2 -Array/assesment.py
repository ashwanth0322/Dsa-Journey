#Creating a program which works on both leader follower and count occurence pattern 
def lar_occurence(arr):
    largest=arr[0]
    count=0
    for i in arr[1:]:
        if i > largest:
            largest=i
            count=0
        if i == largest:
                count+=1
    return largest,count
arr=[4,7,9,12,11,7,12,12]
print(lar_occurence(arr))

    
         