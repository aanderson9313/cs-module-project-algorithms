'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    res_arr = []
    i = 0
    j = k
    
    while i <= len(nums) - k:
        sliding_window = nums[i:j]
        res_arr.append(max(sliding_window))
        i += 1
        j += 1
        
    return res_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
