import os

def get_values():
	#returns settings in a dictionary
	config_file={'config':'values'}
	file=open(os.environ['HOME']+'/.ircyka','rw');
	for line in file:
		if '=' in line:
			name=line.split('=')[0]
			value=line.split('=')[1].strip('\n ')
			config_file[name]=value
	file.close()
	return config_file

def set_value(values):
	#saves settings from dictionary values
	#currently does nothing
	pass
