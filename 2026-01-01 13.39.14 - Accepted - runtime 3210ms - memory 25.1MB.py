class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        from collections import Counter
        
        need = Counter(word2)
        have = Counter()
        
        required = len(need)
        formed = 0
        
        result = 0
        left = 0
        n = len(word1)
        
        for right in range(n):
            c = word1[right]
            have[c] += 1
            
            if c in need and have[c] == need[c]:
                formed += 1
            
            # When we have all required characters
            while formed == required:
                # All substrings from [left, right] to [left, n-1] are valid
                result += n - right
                
                # Shrink window from left
                left_char = word1[left]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        
        return result