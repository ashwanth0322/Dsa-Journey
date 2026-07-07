#Solving the program using count occurence pattern 
def count_occurrences(arr, target):
    count=0
    for i in arr:
        if i == target:
            count+=1
    return count
arr = [5, 2, 5, 1, 5]
target = 5
print(f"the number of times {target} occuring is {count_occurrences(arr,target)}")

