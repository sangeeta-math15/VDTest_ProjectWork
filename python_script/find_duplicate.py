
# Algorithm (Binary Search on the range)
def findDuplicate(nums):
    low, high = 1, len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        count = sum(num <= mid for num in nums)

        if count > mid:
            high = mid
        else:
            low = mid + 1

    return low


input_arr = [1, 3, 4, 2, 2]
print(findDuplicate(input_arr))
