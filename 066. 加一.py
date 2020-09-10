# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/plus-one
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    @classmethod
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        while 1:
            if i == -len(digits)-1:
                digits.insert(0,1)
                return digits
            if digits[i] < 9:
                digits[i]+=1
                return digits
            else:
                digits[i] = 0
                i-=1
print(Solution.plusOne([9,9,9]))