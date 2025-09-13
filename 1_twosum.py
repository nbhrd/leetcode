class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # x = len(nums)
        # for i in range(x):
        #     for j in range(i+1, x):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        dict = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return[i, dict[target - nums[i]]]
            dict[nums[i]] = i