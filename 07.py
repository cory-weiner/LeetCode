class Solution:
    def reverse(self, x: int) -> int:
        start_idx = 0
        mult = 1
        if x < 0:
            start_idx = 1
            mult = -1
        result = mult*int(str(x)[start_idx:][::-1])
        if result < -2147483648 or result > 2147483647:
            result = 0
        return result