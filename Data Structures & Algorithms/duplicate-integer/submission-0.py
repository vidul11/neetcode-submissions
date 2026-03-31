class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_map = set()
        for x in nums:
            if x in seen_map:
                return True
            seen_map.add(x)
        return False 
