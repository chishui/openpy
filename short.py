import os
import json
import sys
from operation import Operation as OP

cur_directory = os.path.dirname(sys.argv[0] if len(sys.argv) else os.path.abspath(__file__))

class Shortcut(object):

	short_config_file = os.path.join(cur_directory, "short.json")

	def __init__(self) :
		with open(self.short_config_file) as f:
			self.config = json.loads(f.read())

	def __flush__(self) :
		with file(self.short_config_file, 'w') as f:
			f.write(json.dumps(self.config))	

	def add_shortcut(self, short, cmd) :
		if short not in self.config['cmd']:
			self.config['cmd'][short] = []
		self.config['cmd'][short].append(cmd)
		self.__flush__()

	def remove_shortcut(self, short, cmd):
		if short in self.config['cmd']:
			if cmd:
				if cmd in self.config['cmd'][short]:
					del self.config['cmd'][short][cmd]
			else:
				del self.config['cmd'][short]
			self.__flush__()

	def get_cmds(self, short = None) :
		if short:
			if short in self.config['cmd']:
				return self.config['cmd'][short]
			else:
				return []
				
		return self.config['cmd']

