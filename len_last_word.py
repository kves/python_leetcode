class Solution:
    def lengthOfLastWord(s: str) -> int:
        s = s.strip()
        last_word_length = 0
        i = len(s) - 1
        if i == 0:
            return 1
        else:
            while i >= 0:
                last_word_length += 1
                i -= 1
                if s[i] == ' ':
                    break
        return last_word_length
    

s = "a"
print(Solution.lengthOfLastWord(s))