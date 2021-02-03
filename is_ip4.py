def is_ipv4(ip):
	a = ip.split('.') if len(ip.split('.')) == 4 else []
	if not a:
		return False
	for i in a:
		if i.isalpha() or not (0 <= int(i) <= 255):
			return False
	return True

# ------------------------- test -------------------------

a = [
	'100.100.100.100',
	'192.168.2.10',
	'10.20.30.400',
	'169.254.1.1',
	'this isn\'t an ip address',
	'a.b.c.d',
	'0.0.0.0',
	'255.0.255.0',
	'170.165.2.201.87',
	]
for i in a:
	print('\n' + i + ' - ' + str(is_ipv4(i)))
input()