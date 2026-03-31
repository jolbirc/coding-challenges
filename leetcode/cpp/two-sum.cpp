/* Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to target
*/

#include <vector>
#include <iostream>

class Solution
{
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target)
    {
        for (auto it = nums.begin(); it != nums.end(); ++it)
        {
            if (target < nums[*it])
            {
                nums.erase(nums.begin() + *it);
            }
        }

        for (auto i = nums.begin(); i != nums.end(); ++i)
        {
            for (auto j = nums.begin(); j != nums.end(); ++j)
            {
                if (nums[*i] + nums[*j] == target)
                {
                    return std::vector<int>(nums[*i], nums[*j]);
                }
            }
        }

        return std::vector<int> (0);
    }
}
