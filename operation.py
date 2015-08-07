
import os
class Operation:

	def open(self, path) :
		os.system("open \"" + path+"\"")

	def run(self, cmd) :
		os.system(cmd)