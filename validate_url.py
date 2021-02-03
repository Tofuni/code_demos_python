import requests as req

def validate_url(url):
	try:
		a = req.get(url)
		sc = a.status_code
		if str(sc)[0] == '2':
			s = 'success'
		else:
			s = 'info'
		r = {'url':url, 'status':s, 'status_code':sc}
		print(str(r) + '\n')
		return r
	except Exception as e:
		print('error - ' + str(e) + '\n')

# -------------------- test -------------------

validate_url('http://fbacarisas.com')
validate_url('https://aws.amazon.com')
validate_url('https://www.weather.com')
validate_url('https://requests.readthedocs.io/en/master/')
validate_url('https://wikipedia.com')
validate_url('https://fbacarisas1234.com')
validate_url('random_string')
validate_url('https://youtube.com')
validate_url('https://docs.google.com/document/')

input()
