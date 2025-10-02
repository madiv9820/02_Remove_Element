from typing import List

class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        # 🎒 Prepare a fresh bag to collect the good stuff
        elements_other_than_val = []

        # 🕵️‍♂️ Scan through the original list for the "bad guy"
        for index in range(len(nums)):
            if nums[index] != val: 
                # 👍 If it's not the villain (val), we keep it!
                elements_other_than_val.append(nums[index])

        # 🛠️ Now, overwrite the original list with our filtered heroes
        for index in range(len(elements_other_than_val)):
            nums[index] = elements_other_than_val[index]

        # 📏 Return the count of brave survivors
        return len(elements_other_than_val)