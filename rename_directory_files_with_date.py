import os
import datetime as dt

# params: (path) string path
def rename_directory_files_with_date(path):
	try:
		files = os.listdir(path)
		d = dt.datetime.now().strftime('%d%m%Y')+'_'
		for file in files:
			os.rename(path+file, path+d+file)
		return
	except Exception as e:
		print(e)

# ----------------------- test -----------------------

print('\n\ndirectory files: ' + str(os.listdir('./test')) + '\n\n----------------------\n\n')

rename_directory_files_with_date('./test/')

print('directory files: ' + str(os.listdir('./test')))

input()