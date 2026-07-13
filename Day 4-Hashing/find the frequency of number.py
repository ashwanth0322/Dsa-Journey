#Create a code that finds the frequency of number
def find_frequency(arr):
    freq={}
    unique=[]
    for i in arr:
        if i not in freq:
            freq[i]=1
        elif i in freq:
            freq[i]+=1
    for i in freq:
        if freq[i] == 2:
            unique.append(i)
    return unique
            
arr = [2,5,2,8,5,5,9,9,1]
print(find_frequency(arr)) 