class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map, left, max_len ={}, 0, 0
        for right in range(len(s)):
            curr_char = s[right]
            if curr_char in char_map and char_map[curr_char]>=left:
                left = char_map[curr_char]+1
            char_map[curr_char] = right
            current_window = right - left + 1
            if current_window>max_len:
                max_len=current_window
        return max_len
