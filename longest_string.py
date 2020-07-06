
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_uniq = list(s)
        a = {}
        for i,j in enumerate(s_uniq):
            if j not in list(a.keys()):
                a[j] = [i]
            else:
                a[j].append(i)
        Max = 0
        count = 0  # 用来统计是不是没有重复的
        for i in list(a.keys()):
            res,count = self.max_sub(count,a[i])
            if count == len(s_uniq):
                Max = len(s_uniq)
                break
            elif res > Max:
                Max = res
        return Max

    def max_sub(self,count,List):
        res = []
        i = 0
        if len(List) > 1:
            while i + 1 < len(List):
                sub = List[i + 1] - List[i]
                res.append(sub)
                i += 1
        else:
            res.append(1)
            count += 1
        return max(res),count'''
#哈希Map 只需一次遍历,
#依次往后移，如果出现不同的，往c_dict里添加字符及其对应的index，并对比字符串长度与，如果相同，用一个k值来代替当前的index，c_dict更新最新的index
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res
#滑动窗法
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        occ = set()
        n = len(s)
        right, ans = 0, 0
        for left in range(n):
            while right < n and s[right] not in occ:
                occ.add(s[right])
                right += 1
            if len(occ) > ans:
                ans = len(occ)
            occ.remove(s[left])
        return ans

if __name__ == "__main__":
    a = Solution1()
    b = a.lengthOfLongestSubstring("awwscw")
    print(b)
#aab
#aw
