def matching_substr(txt1, txt2):
	r = []
	for i in range(len(txt1)):
		for j in range(len(txt2)):
			if txt1[i] == txt2[j]:
				isMatch = True
				count = 1
				while isMatch:
					isMatch = False
					if i+count > len(txt1) or j+count > len(txt2):
						break
					c1 = txt1[i:i+count]
					c2 = txt2[j:j+count]
					if c1 == c2:
						isMatch = True
						count += 1
						r.append(c1)
	return r

print(matching_substr("catfish sands", "cats and fish"))
input()