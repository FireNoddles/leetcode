# 颠倒给定的 32 位无符号整数的二进制位。
#
#  
#
# 示例 1：
#
# 输入: 00000010100101000001111010011100
# 输出: 00111001011110000010100101000000
# 解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
#      因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-bits
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0

        for i in range(32):
            # z这一步一定放在前面不然会变成33步
            ans = ans << 1
            a = n & 1
            ans = ans | a
            n = n >> 1

        return ans

print(10|0)
