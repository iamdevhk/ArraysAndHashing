class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_list = set(nums)
        if len(set_list) < len(nums):
            return True
        else:
             return False
        