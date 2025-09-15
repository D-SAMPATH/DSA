class Solution(object):
    def subarraySum(self, nums, k):
        hashmap = {0:1}
        current_sum = 0
        count = 0
        for num in nums :
            current_sum+=num
            if current_sum - k in hashmap:
                count+=hashmap[current_sum - k]
            hashmap[current_sum] = hashmap.get(current_sum,0)+1
        return count

        