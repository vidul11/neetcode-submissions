class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in map and map[diff] != index: # main check if the second value (diff) is present and if the index of diff and current i is not same
                return [min(index, map[diff]),max(index, map[diff])]

            map[value] = index # adds values and indexs into the map. Normally its key:value pairs but for us we need the answer to be indices not the value so the pairing will be value:indices
            



           