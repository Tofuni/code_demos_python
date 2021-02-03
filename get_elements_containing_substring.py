def get_elems_with_substr(a, s):
	return [r for r in a if r.find(s) != -1]

# --------------------------------- test ---------------------------------
	
a = [
	[['dorado', 'crab', 'fish', 'salmon', 'shrimp', 'dab'], 'ab'],
	[['koko da yo', 'wakaranai', 'cotton candy ei ei oh', 'asoko', 'neo sky, neo map', 'kore wa pen desu'], 'ko'],
	[['märchen mädchen', 'magical girl lyrical nanoha', 'cardcaptor sakura', 'yuki yuna is a hero', 'madoka magica', 'flip flappers', 'magia record'], 'magic'],
	[['zombieland saga', 'the idolm@ster cinderella girls', 'wake up girls', 'dropout idol fruit tart', 'nanabun no nijyuuni', 'nijigasaki school idol club'], 'idol']
	]

for i in a:
	print('\n' + str(i[0]) + '\n\nget items with substr: ' + str(i[1]) + '\n\n' + str(get_elems_with_substr(i[0], i[1])) + '\n\n----------------------------------')
input()