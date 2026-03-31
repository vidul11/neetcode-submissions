class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range (len(nums) + 1)] #setting the range of main bucket sort to be same as nums+1

        for x in nums:
            count[x] = 1 + count.get(x, 0) # getting the counts for each x
        for x, c in count.items():
            bucket[c].append(x) #main step of setting up our bucket sort, flipping the key:value pairs to count:x(value)

        frequent_k = []

        for j in range (len(bucket)-1 , 0 , -1): #setting up range to come from right to left of array (from the end)
            for x in bucket[j]:
                frequent_k.append(x) #updating all the values with the top counts
                if len(frequent_k) == k:
                    return frequent_k 


