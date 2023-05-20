from mainActions import *
import modules.gestException as exception
import sys

try:
	clearFile('editorException.txt')
	start()

	import random
	
	s = 'eeeee' + '55'
	angle(BASE, 45)
	print('ciao')
	sleep(1)
	reset()
	for x in range(150):
		angle(BASE, x)
	stop()
	sleep(1)
	start()
	for x in range(150):
		angle(random.randint(1, 3), x)
	
	
	#angle(PINZA, 100)
	print('fine')
except BaseException as e:  # eccezione madre di tutti gli Error e le Exception
	shutdown()
	print('qui')
	
	#exception.onExcept(sys.exc_info(), lcd)
