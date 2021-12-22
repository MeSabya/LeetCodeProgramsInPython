def backspace_compare(self, S, T):
	s = []
	t = []
	for c in S:
		if c == '#':
			if s != []:
				s.pop()
		else:
			s.append(c)
	for c in T:
		if c == '#':
			if t != []:
				t.pop()
		else:
			t.append(c)
	return s == t
	

def main():
  print(backspace_compare("xy#z", "xzz#"))
  print(backspace_compare("xy#z", "xyz#"))
  print(backspace_compare("xp#", "xyz##"))
  print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()


# Complexity : O(M+N) , where M , N = length of S and T

