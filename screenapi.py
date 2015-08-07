
import curses
class ScreenAPI(object) :

	def __init__(self) :
		self.stdscr = curses.initscr()

	def quit(self) :
		curses.nocbreak()
		self.stdscr.keypad(False)
		curses.echo()
		curses.endwin()

	def pre_run(self) :
		curses.noecho()
		curses.cbreak()
		curses.curs_set(0) 
		self.stdscr.keypad(True)

if __name__ == '__main__':
	api = ScreenAPI()
	while True: 
		event = api.stdscr.getch() 
		if event == ord("q"): 
			break  	
	api.quit()