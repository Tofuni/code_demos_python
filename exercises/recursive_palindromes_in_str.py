def recursive_palindromes_in_str(text):
	r = []
	def eval_palindrome(current, text, r):
		if len(current) > 1 and current == current[::-1]:
			if current not in r:
				r.append(current)
		for idx in range(len(text)):
			eval_palindrome(current+text[idx], text[idx+1:], r)
			current = ""
	eval_palindrome("", text, r)
	return r

print(recursive_palindromes_in_str("abcdcbadxvwxyzyxwv"))
print(recursive_palindromes_in_str("oasis kayaks"))
input()