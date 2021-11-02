def longest_substring_with_k_distinct(str1, k):
    window_start, max_len = 0, 0
    char_freq_map = {}
    
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_freq_map:
            char_freq_map[right_char] = 0
        
        char_freq_map[right_char] +=1
        
        while len(char_freq_map)>k:
            start_char = str1[window_start]
            window_start +=1
            char_freq_map[start_char]-=1
            if char_freq_map[start_char] == 0:
                del char_freq_map[start_char]
        
        max_len = max(max_len, window_end-window_start+1)
        
    return max_len

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
        