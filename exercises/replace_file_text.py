def replace_file_text(file, textToReplace, newText):
	rfile = open(file)
	lines = rfile.readlines()
	newLines = list(map(lambda line: line.replace(textToReplace, newText), lines))
	rfile.close()
	
	wfile = open(file, mode='w')
	wfile.write("".join(newLines))
	wfile.close()
	return

replace_file_text("./file1.txt", "hello", "greetings")
