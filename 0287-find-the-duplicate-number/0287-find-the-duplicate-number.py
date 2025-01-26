class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0] # or 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast: # slow == fast means there is a cycle (i.e., some number repeated)
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = nums[0] # or 0
        while slow != fast: # According to floyd, distance from current slow and new fast (moving at speed 1) to number that led to cycle is equal and meet exactly at that number again
            slow = nums[slow]
            fast = nums[fast]
        return slow