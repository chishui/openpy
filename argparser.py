import argparse
class ArgParser(object) :

	def __init__():
		pass

	@staticmethod
	def get_arg_parser() :

		usage = '''opy [-h] [-ap ADD_PATH] [-rp REMOVE_PATH] [-as ADD_SHORTCUT -d DESTINATION]
           [-rs REMOVE_SHORTCUT] [--version]
'''

		parser = argparse.ArgumentParser(prog='opy', usage=usage)
		parser.add_argument('-ap',
							'--add-path',
							help='''
Add path to config file, so next time do quick open file will search files in this path''')
		parser.add_argument('-rp',
							'--remove-path',
							help='''
Remove path from config file, so next time do quick open won't search files in this path''')
		parser.add_argument('-sp',
							'--show-path',
							default=False,
                            action='store_true',
							help='''
Show all paths in config file''')

		parser.add_argument('-as',
							'--add-shortcut',
							help='''
Add a shortcut to some file or command, so next time could open file or execute command using "opy @<shortcut>" ''')
		parser.add_argument('-d',
							'--destination',
							help='''
Destination path or command for shortcut''')
		parser.add_argument('-rs',
							'--remove-shortcut',
							help='''Remove shortcut''')
		parser.add_argument('-ss',
							'--show-shortcut',
							help='''show shortcut''')
		parser.add_argument('-sas',
							'--show-all-shortcut',
							default=False,
							action='store_true',
							help='''show all shortcut''')
		parser.add_argument('-a',
							'--auto-open',
							#default=1,
							type=int,
							help='''Set true when single one file or command matched, auto open''' )
		parser.add_argument('--version',
							default=False,
							help='''
Print the version of opy and exit.''',
							action='store_true')	
		return parser	