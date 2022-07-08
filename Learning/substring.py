class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == '' : return 0
        start = 0
        i = 0
        max_length = 0
        unique_characters = set()
        while i < len(s):
            if s[i] not in unique_characters:
                print('Added: ', s[i], i)
                unique_characters.add(s[i])
                i += 1
                max_length = max(max_length, len(unique_characters))

            else:
                print('Removed: ', s[start], start)
                unique_characters.remove(s[start])
                start += 1

        return max_length

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
