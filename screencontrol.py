import sys
import curses
from screenapi import ScreenAPI

class ScreenControl(object) :
	
	LEFT_OFFSET  = 4
	
	TEXT_NORMAL  = curses.A_UNDERLINE
	
	TEXT_REVERSE = curses.A_REVERSE

	def __init__(self, items) :
		self.items = items
		self.screenAPI = ScreenAPI()
		self.cur = -1
		self.select_item = None

	def __del__(self) :
		self.screenAPI.quit()

	def __run__(self) :
		while True: 
			event = self.screenAPI.stdscr.getch() 
			if event == ord("q"): 
				break  
			elif event == curses.KEY_UP: 
				if len(self.items) == 1: continue
				self.toggle(self.cur)
				newindex = self.cur - 1
				if newindex < 0:
					newindex = len(self.items) - 1
				self.toggle(newindex)

			elif event == curses.KEY_DOWN:
				if len(self.items) == 1: continue
				self.toggle(self.cur)
				newindex = self.cur + 1
				if newindex >= len(self.items):
					newindex = 0
				self.toggle(newindex)

			elif event == curses.KEY_ENTER or event == 10:
				self.select(self.cur)	
				break		

		self.quit()

	def get_show_text(self, index) :
		return self.items[index]['show']

	def show(self) :
		for i, item in enumerate(self.items):
			self.screenAPI.stdscr.addstr(i, 0, '['+str(i + 1)+']'.ljust(self.LEFT_OFFSET), curses.A_NORMAL)
			self.screenAPI.stdscr.addstr(i, self.LEFT_OFFSET, self.get_show_text(i), self.TEXT_NORMAL)

		self.toggle(0)
		self.screenAPI.pre_run()
		self.__run__()

	def quit(self) :
		self.screenAPI.quit()

	def toggle(self, index) :
		if self.cur == index:
			self.screenAPI.stdscr.chgat(index, self.LEFT_OFFSET, len(self.get_show_text(index)), self.TEXT_NORMAL)
		else:
			self.screenAPI.stdscr.chgat(index, self.LEFT_OFFSET, len(self.get_show_text(index)), self.TEXT_REVERSE)
			self.cur = index
		self.screenAPI.stdscr.refresh()

	def select(self, index) :
		self.select_item = self.items[index]


