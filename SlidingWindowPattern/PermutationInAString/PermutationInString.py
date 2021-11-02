def find_permutation(str1, pattern):
    char_freq_map = {}
    window_start, matched = 0, 0
    
    for chr in pattern:
        if chr not in char_freq_map:
            char_freq_map[chr] = 0
        char_freq_map[chr] += 1
        
    
    for window_end in range(len(str1)):
        curr_char = str1[window_end]
        if curr_char in char_freq_map:
            char_freq_map[curr_char] -=1
            if char_freq_map[curr_char] == 0:
                matched +=1
        
        if matched == len(char_freq_map):
            return True
        
        if window_end >= len(pattern)-1:
            start_char = str1[window_start]
            window_start +=1
            
            if start_char in char_freq_map:
                if char_freq_map[start_char] == 0:
                    matched = -1
                char_freq_map[start_char] +=1
    return False

def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
