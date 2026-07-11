#Create code to check wheather the given array is sorted or not
def is_sorted(arr):
   
   for i in range(len(arr)):
      if i+1 < len(arr):
        if arr[i] <= arr[i+1]:
            pass
        else:
            return False
   return True
        
arr=[2,1,4,5,6]
print(is_sorted(arr))
         
         
       
      