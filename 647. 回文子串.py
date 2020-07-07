# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
#
# 示例 1:
#
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindromic-substrings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0 for i in range(len(s))] for i in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(1, len(s)):
            for j in range(i):
                if s[i] == s[j]:
                    if i - j <= 2:
                        dp[j][i] = 1
                    else:
                        if dp[j + 1][i - 1] == 1:
                            dp[j][i] = 1
        ans = 0
        for _ in dp:
            ans += sum(_)
        return ans
