import unittest
from timeout_decorator import timeout
from Solution import Solution

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = (
            ([3,2,2,3], 3, 2, [2,2]),
            ([0,1,2,2,3,0,4,2], 2, 5, [0,1,3,0,4])
        )
        self.__solution = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_0(self):
        nums, val, output, result = self.__testcases[0]
        size: int = self.__solution.removeElement(nums = nums, val = val)
        self.assertEqual(size, output)
        self.assertTrue(all(a == b for a, b in zip(result, nums[:len(result)])))
    
    @timeout(0.5)
    def test_case_1(self):
        nums, val, output, result = self.__testcases[1]
        size: int = self.__solution.removeElement(nums = nums, val = val)
        self.assertEqual(size, output)
        self.assertTrue(all(a == b for a, b in zip(result, nums[:len(result)])))

if __name__ == '__main__': unittest.main()