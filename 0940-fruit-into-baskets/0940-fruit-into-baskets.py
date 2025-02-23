class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        l = 0
        max_fruits = 0
        for r in range(len(fruits)):
            if fruits[r] not in count:
                count[fruits[r]] = 0
            count[fruits[r]] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if not count[fruits[l]]:
                    count.pop(fruits[l])
                l += 1
            max_fruits = max(max_fruits, r - l + 1)
        return max_fruits