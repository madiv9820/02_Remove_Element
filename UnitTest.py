import unittest
from timeout_decorator import timeout
from Solution import Solution

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = (
            ([3,2,2,3], 3, 2, [2,2]),
            ([0,1,2,2,3,0,4,2], 2, 5, [0,1,3,0,4])
        )
        self.__object = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_0(self):
        nums, val, actual_size, actual_nums = self.__testcases[0]
        result_size = self.__object.removeElement(nums = nums, val = val)
        self.assertEqual(actual_size, result_size)
        self.assertTrue(all(a == b for a, b in zip(nums[:actual_size], actual_nums)))
    
    @timeout(0.5)
    def test_case_1(self):
        nums, val, actual_size, actual_nums = self.__testcases[1]
        result_size = self.__object.removeElement(nums = nums, val = val)
        self.assertEqual(actual_size, result_size)
        self.assertTrue(all(a == b for a, b in zip(nums[:actual_size], actual_nums)))

if __name__ == '__main__': unittest.main()