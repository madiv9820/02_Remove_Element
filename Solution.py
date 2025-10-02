from typing import List

class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        # 🎯 This is where we'll place our good citizens (not equal to val)
        actual_index = 0

        # 🕵️‍♂️ Let's investigate each element in the array
        for current_index in range(len(nums)):
            if nums[current_index] != val:
                # ✅ Found someone who isn't the target! Move them forward!
                nums[actual_index] = nums[current_index]
                actual_index += 1  # Advance the safe zone 🛡️
        
        # 🧮 Return the number of non-val elements — our new array size!
        return actual_index