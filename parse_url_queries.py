def url_query(q):
	a = q[q.find('?')+1::]
	r = {}
	while(a.find('&') != -1):
		r[ a[0:a.find('=')] ] = a[a.find('=')+1:a.find('&')]
		a = a[a.find('&')+1::]
	r[ a[0:a.find('=')] ] = a[a.find('=')+1::]
	return r
		
# ----------------------- test -----------------------

a = [
	'https://www.amazon.com/gp/css/homepage.html?ie=UTF8&ref_=nav_youraccount_ya',
	'https://www.aws.training/LearningLibrary?filters=classification%3A67&filters=classification%3A2&search=&tab=digital_courses',
	'https://academy.microsoft.com/en-us/dashboard/?EnrollTrackSlug=artificial-intelligence',
	'https://www.udemy.com/courses/search/?src=ukw&q=python&p=1&duration=extraLong&ratings=4.0&instructional_level=all',
	'https://store.steampowered.com/search/?term=%E6%9D%B1%E6%96%B9&category1=998&category3=2&supportedlang=japanese',
	'https://finance.yahoo.com/quote/NTDOY/profile?p=NTDOY&.tsrc=fin-srch',
	'https://www.google.com/search?q=dictionary&oq=dictionary&aqs=chrome..69i57j0l5.1383j0j7&sourceid=chrome&ie=UTF-8#dobs=happiness',
	'http://fbacarisas.com/'
	]
for i in a:
	print('\n' + i + '\n\n' + str(url_query(i)) + '\n\n ------------------------ \n')
input()