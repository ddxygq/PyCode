from configparser import ConfigParser

def getConfig(file_name, encoding='utf-8'):
	config = {}
	cf = ConfigParser()
	cf.read(file_name, encoding=encoding)
	sections = cf.sections()
	for section in sections:
		options = cf.options(section)
		for option in options:
			config[section+option] = cf.get(section, option)
	return config