def longest_subarray(arr, k):
    prefix_sum = 0
    maximum = 0
    prefix_map = {}

    for i in range(len(arr)):
        prefix_sum+=arr[i]
        if prefix_sum == k:
            maximum=max(maximum,i+1)
        
        required=prefix_sum-k
        if required in prefix_map:
                lenght=i-prefix_map[required]
                maximum=max(maximum,lenght)
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum]=i
        
            
    return maximum
arr=[1,2,2,2,1,1,1,1]
print(longest_subarray(arr,4))
        