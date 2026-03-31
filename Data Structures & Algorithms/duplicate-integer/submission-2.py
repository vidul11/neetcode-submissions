class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Using set() (hashing): it acts as a store to check each value if already seen or not
        seen = set()

        for i in nums:
            if i in seen:
                return True
            
            seen.add(i)

        return False

