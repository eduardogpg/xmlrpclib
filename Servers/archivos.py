from os import listdir

for archivo in listdir("."):
	if archivo[-2:] != 'py':
		print archivo