import os
import re
import sys
import subprocess
from config import Config
from short import Shortcut
from sys import platform as _platform
from screencontrol import ScreenControl
from argparser import ArgParser


# class OpenPy(object) :
# 	def __init__(self) :
# 		self.get_platform_object()

# 	def __get_platform_object__(self):
# 		if _platform == "darwin":# OS X
# 			from platform.mac import MacPlatform
# 			self.platform = MacPlatform()
# 		elif _platform == "win32": # Windows
# 			from platform.windows import WindowsPlatform
# 			self.platform = WindowsPlatform()

def runner(item):
	print item
	if os.path.exists(item):
		os.system('open '+'\"'+item+'\"')
	else:
		os.system(item)

def comparator(src, des) :
	newdes = ''.join(['.'+i if i == '*' else i for i in list(des)])
	return re.match(newdes, src) != None

def search_file(name) :
	files = []
	for _ in paths:
		for src in os.listdir(_):
			if comparator(src, name) :
				files.append(os.path.join(_, src))
	return files

def find_file(name) :
	"""
	Someone did a research on speed comparison of os.walk and 'find' command in linux,
	and 'find' won. see https://burnsed.wordpress.com/2013/12/19/python-os-walk-vs-linux-find/
	"""
	#TODO here may need multi-threaded
	files = []
	config = Config()
	for path in config.path():
		cmd = [ 'find', path,'-maxdepth','1','-iname', name ]
		output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
		files = files + output.split('\n')

	files = [_ for _ in files if len(_)]
	return files	

def add_path(path) :
	c = Config()
	c.add_path(path)

def remove_path(path) :
	c = Config()
	c.remove_path(path)

def show_path():
	c = Config()
	for path in c.path():
		print path

def add_shortcut(shortcut, cmd) :
	s = Shortcut()
	s.add_shortcut(shortcut, cmd)

def remove_shortcut(shortcut, cmd = None) :
	s = Shortcut()
	s.remove_shortcut(shortcut, cmd)

def run_shortcut(shortcut) :
	s = Shortcut()
	cmds = s.get_cmds(shortcut)
	if len(cmds) == 1:
		c = Config()
		if c.is_auto():
			#TODO RUN
			pass
			return
	items = []
	for file in cmds:
		items.append({'show' : file})
	control = ScreenControl(items)
	control.show()	
	if control.select_item:
		runner(control.select_item['show'])

def show_shortcut(shortcut) :
	s = Shortcut()
	cmds = s.get_cmds(shortcut)
	if len(cmds) > 0:
		print "for shortcut:\"" + shortcut + "\":\n"
		for cmd in cmds:
			print cmd
	else:
		print "no items for shortcuts:",shortcut

def show_all_shortcut():
	s = Shortcut()
	cmds = s.get_cmds()
	if len(cmds) > 0:
		for k,v in cmds.items():
			print "for shortcut:",k
			for i in v:
				print "\t",i
	else:
		print "no shortcuts"

def openpy(name) :
	files = find_file(name)
	if len(files) == 0:
		print 'nothing found!'
	elif len(files) == 1:
		runner(files[0])
	else:
		if len(files) > 10:
			files = files[0:10]
		items = []
		for file in files:
			items.append({'show' : file})
		control = ScreenControl(items)
		control.show()
		control.quit()
		if control.select_item:
			runner(control.select_item['show'])

def set_auto(is_auto) :
	c = Config()
	c.set_auto(is_auto)
	
def parse(argv):
	def help(parser) :
		parser.print_help()
		sys.exit(0)

	parser = ArgParser.get_arg_parser()
	if len(argv) <= 1:
		help(parser)
	
	(args, chars) = parser.parse_known_args(argv)

	if args.add_path:
		add_path(args.add_path)
	elif args.remove_path:
		remove_path(args.remove_path)
	elif args.show_path:
		show_path()
	elif args.add_shortcut:
		if args.destination:
			add_shortcut(args.add_shortcut, args.destination)
		else:
			help(parser)
	elif args.remove_shortcut:
		remove_shortcut()
	elif args.show_shortcut:
		show_shortcut(args.show_shortcut)
	elif args.show_all_shortcut:
		show_all_shortcut()
	elif args.destination:
		help(parser)
	elif args.auto_open == True or args.auto_open == False:
		set_auto(args.auto_open)
	else:
		if len(chars) < 1:
			help(parser)
		else:
			text = chars[1]
			if text[0] == '@':
				run_shortcut(text[1:])
			else:
				openpy(text)



if __name__ == '__main__':
	parse(sys.argv)
