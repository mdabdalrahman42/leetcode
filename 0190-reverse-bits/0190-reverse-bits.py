class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for _ in range(32):
            output <<= 1
            output += n % 2
            n >>= 1
        return output