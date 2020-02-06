class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str: return 0
        mult = 1
        if str[0] == "+":
            str = str[1:]
        elif str[0] == '-':
            mult = -1
            str = str[1:]
        output_str = ''
        for char in str:
            if char in ['0','1','2','3','4','5','6','7','8','9']:
                output_str += char
            else:
                break
        if not output_str:
            output_str = '0'
        result = mult*int(output_str)
        if result < -2147483648:
            result = -2147483648
        if result > 2147483647:
            return 2147483647
        return result