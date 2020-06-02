class Solution:
    # time cost: o(n*max_len)
    # space cost: o(1)
    def longestWord(self, words: List[str]) -> str:
        def f(word):
            for i in range(len(word)):
                left = word[:i]
                right = word[i:]
                if left in words:
                    if right in words:
                        return True
                    elif f(right):
                        return True
                    else:
                        continue
                else:
                    continue
            return False
        
        res = ''
        for word in words:
            if f(word):
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):
                    res = min(res, word)
        return res