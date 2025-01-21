class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        nums = [1,3,4,2,2]
        indi = [0,1,2,3,4]

        Linked List is 1 -> 3 (nums[1]) -> 2 (nums[3]) -> 4 (nums[2]) -> cycle to 2 again and so on...
        Linked List can be made based on indices too
        For the above list, initially slow pointer moves 1 step and fast moves 2 steps starting from first element
        """
        slow = nums[0] # 0 if based on indices
        fast = nums[0] # 0 if based on indices
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # According to floyd, if element e is starting point of a cycle, distance from current slow to this e is same as distance from fast starting from 1st element of LL and moving 1 step ahed to this e i.e., fast and slow intersect at e at certain point of time
        fast = nums[0] # 0 if based on indices
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow