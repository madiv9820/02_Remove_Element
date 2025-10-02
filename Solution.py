from typing import List

class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        # 🚀 Initialize our mission variables
        n = len(nums)  # Total number of elements before battle begins 🧮
        no_of_elements_deleted = 0  # Our kill count 💀
        current_index = 0  # Where we are currently scanning with our 👀
        last_index = len(nums) - 1  # The last known survivor's position 🎯

        # 🏃 Begin our glorious loop through the battlefield
        while current_index <= last_index:
            if nums[current_index] == val:  # Found an enemy soldier! ⚔️
                # Shift everyone after the enemy one step to the left 👉
                for index in range(current_index + 1, last_index + 1):
                    nums[index - 1] = nums[index]
                # Update the last survivor’s index and log the kill 🔄💀
                last_index -= 1
                no_of_elements_deleted += 1
            else:
                # Just a friendly civilian, move along 👋
                current_index += 1

        # Mission accomplished 🎖️ — Return number of survivors 🧍‍♂️🧍‍♀️
        return n - no_of_elements_deleted