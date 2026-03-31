class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range (len(nums) + 1)]

        for x in nums:
            count[x] = 1 + count.get(x, 0)
        for x, c in count.items():
            bucket[c].append(x)

        frequent_k = []

        for j in range (len(bucket)-1 , 0 , -1):
            for x in bucket[j]:
                frequent_k.append(x)
                if len(frequent_k) == k:
                    return frequent_k 


