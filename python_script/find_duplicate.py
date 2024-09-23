# Floyd's Tortoise and Hare algorithm
def findDuplicate(nums):
    slow_pointer = nums[0]
    fast_pointer = nums[0]

    while True:
        slow_pointer = nums[slow_pointer]
        fast_pointer = nums[nums[fast_pointer]]
        if slow_pointer == fast_pointer:
            break

    slow_pointer = nums[0]
    while slow_pointer != fast_pointer:
        slow_pointer = nums[slow_pointer]
        fast_pointer = nums[fast_pointer]

    return fast_pointer


input_arr = [1, 3, 4, 2, 2]
print(findDuplicate(input_arr))
