import datetime as dt

# params: (content) string to write to file
def datestamp_file(content=''):
	d = dt.datetime.now()
	f = open(str(d.strftime('%d')+'-'+d.strftime('%m')+'-'+d.strftime('%Y')+'.txt'),'w+')
	f.write(content)
	f.close()

datestamp_file(content='hello world\nthis is a test')
input()