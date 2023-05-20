try:
	import RPi.GPIO as pi
	from time import sleep
except:
	raise Exception("Libraries are missing")

pi.setmode(pi.BCM)


class Init:

	def __init__(self, pin):
		
		self.length = 40 #Pulse count / While loop count.
		self.pin = int(pin)
		pi.setup(self.pin, pi.OUT)
		pi.output(self.pin, False)
		
	def run(self, degree):
		
		if degree < 0: degree = 0
		if degree > 180: degree = 180

		ms = 0.001 / 100 * (degree * 100 / 90)
		ms = 0.001 + ms

		count = 0
		while count < self.length:
		
			pi.output(self.pin, True)
			sleep(ms)
			pi.output(self.pin, False)
			sleep(0.02 - ms)
			count = count + 1			

		pi.output(self.pin, False)