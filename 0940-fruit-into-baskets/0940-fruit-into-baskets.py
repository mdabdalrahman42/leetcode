class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        total = 0
        l = 0
        count = {}
        for r in range(len(fruits)):
            if fruits[r] not in count:
                count[fruits[r]] = 0
            count[fruits[r]] += 1
            total += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if not count[fruits[l]]:
                    count.pop(fruits[l])
                total -= 1
                l += 1
            max_fruits = max(max_fruits, r - l + 1)
        return max_fruits