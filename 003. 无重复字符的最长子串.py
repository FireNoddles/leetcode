# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# #
# # 示例 1:
# #
# # 输入: "abcabcbb"
# # 输出: 3
# # 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# #
# # 来源：力扣（LeetCode）
# # 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# # 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


#双指针策略

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        max_len = 0
        arr = [s[0]]
        j = 1
        for _ in range(len(s)):
            if _ != 0:
                del arr[0]
            while j < len(s) and self.chongfu(arr, s[j]):
                arr.append(s[j])
                j+=1
            if max_len < len(arr):
                max_len = len(arr)
        return max_len
    def chongfu(self, arr, singer_s):
        if singer_s in arr:
            return False
        else:
            return True