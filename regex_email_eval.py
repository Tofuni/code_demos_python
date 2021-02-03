import re

def regex_email_eval(li, domain):
	valid_emails = []
	for i in li:
		a = re.match("[a-zA-Z0-9]+@"+domain.replace('.','\.')+"$", i)
		if a != None:
			valid_emails.append(a.group(0))
	return valid_emails

# ------------------------- test -------------------------
	
e = [
	'fbacarisas@test.com',
	'something123@test.com',
	'example@amazon.com',
	'example@gmail.com',
	'example@test.com',
	'example@gmail',
	'example.me@test.com',
	'5oceans@test.com',
	'5_oceans@test.com',
	'SOLARsystem@test.com',
	'abcd3f@test.com',
	'user@test',
	'user@test.mail',
	'user@test.com',
	'user@Test.com'
	]
	
e2 = [
	'fbacarisas@email.net',
	'user@test.com',
	'user@email.net',
	'user1234@email.net',
	'user.1234@email.net',
	'user1234@mail.net',
	'user@email',
	'AppL3@email.net'
	]

test_domain = "test.com"
r = regex_email_eval(e, test_domain)

print("\ndomain: " + test_domain)
print('\n\ntest email list:\n')
for x in e:
	print(x)
print('\n\nvalid emails:\n')
for y in r:
	print(y)

print('\n\n_________________________\n\n')

test_domain2 = "email.net"
r2 = regex_email_eval(e2, test_domain2)

print("domain: " + test_domain2)
print('\n\ntest email list:\n')
for x in e2:
	print(x)
print('\n\nvalid emails:\n')
for y in r2:
	print(y)

input()