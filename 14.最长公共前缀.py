#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        pre = "" 
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        first = strs[0]
        for i in range(len(first)):
            pre = first[:i]
            print(pre)
            f = 1 # flag用于跳出外层循环
            for s in strs[1:]:
                if i>=len(s) or s[i] !=  first[i]:
                    f = 0 
                    break
            if f==0:
                break
        return pre

# @lc code=end

