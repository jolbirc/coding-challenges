# Given an array of integers `nums` and `target`, return the indices of the two numbers such that they add up to the target

# Assume that each input would only have one solution

# Answer can be returned in any order

example_nums = [3, 3]
example_target = 6

def twoSum(nums, target):
    nums_list = []
    for num in nums:
        if num <= target:
            nums_list.append(num)
    
    for i in range (0, len(nums_list)):
        current_num = nums_list.pop(i)
        for j in range(0, len(nums_list)):
            if current_num + nums_list[j] == target:
                return nums.index(current_num), nums.index(nums_list[j])


print(twoSum(example_nums, example_target))
