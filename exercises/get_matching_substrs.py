def matching_substr(txt1, txt2):
	r = []
	for i in range(len(txt1)):
		for j in range(len(txt2)):
			if txt1[i] == txt2[j]:
				r.append(txt1[i])
				isMatch = True
				count = 1
				while isMatch:
					isMatch = False
					if i+count == len(txt1) or j+count == len(txt2):
						break
					if txt1[i+count] == txt2[j+count]:
						isMatch = True
						count += 1
						r.append(txt1[i:i+count])
	return r

print(matching_substr("catfish sands", "cats and fish"))
input()