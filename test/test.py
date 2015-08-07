class Test(object) :
	def __init__(self) :
		print "init"

	def __del__(self) :
		print "del"
import math
def main():
	print 100/3
	print math.log(100, 2)*1.44

if __name__ == '__main__':
	main()