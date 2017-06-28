__author__ = 'fteixeira'

import time




class Memento :
	__mem__ = {}
	def __init__(self, f) :
		self.f = f

	def __call__(self, arg) :
		if arg not in self.__mem__ :
			self.__mem__[arg] = self.f(arg)
		return self.__mem__[arg]
start1 = time.time()
def fib1( n ) :
	if n <= 1 :
		return 1
	return fib1(n-1) + fib1(n-2)
end1 = time.time()

start2 = time.time()
@Memento
def fib2( n ) :
	if n <= 1 :
		return 1
	return fib2(n-1) + fib2(n-2)
end2 = time.time()

print(end1-start1)
print(end2-start2)

print 'Computing fib without memento ....', fib1(10)
print 'Computing fib wth memento ....', fib2(20)

a=2

