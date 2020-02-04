# ZigZag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [[] for _ in range(numRows)]
        r_multiplier = 1
        currrent_r = 0
        for index, char in enumerate(s):
            result[currrent_r].append(char)
            if currrent_r == numRows-1:
                r_multiplier = -1 
            elif currrent_r == 0:
                r_multiplier = 1
            currrent_r += (1 * r_multiplier)
            result[currrent_r]
        return ''.join( [''.join(substr) for substr in result])

        
print(Solution().convert('AB',1))