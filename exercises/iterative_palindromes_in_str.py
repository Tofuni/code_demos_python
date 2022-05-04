def iterative_palindromes_in_str(text):
	def is_palindrome(s):
		return s == s[::-1]
	r = []
	c = []
	for letter in text:
		for idx in range(len(c)):
			c[idx] += letter
			if is_palindrome(c[idx]) and c[idx] not in r:
				r.append(c[idx])
		c.append(letter)
	return r

print(iterative_palindromes_in_str("abcdcbadxvwxyzyxwv"))
print(iterative_palindromes_in_str("oasis kayaks"))
input()