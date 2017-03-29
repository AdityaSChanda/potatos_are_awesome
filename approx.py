import math
import random

"""
Aditya S. Chanda
For my function, I've choses f(x) = x^2
because it's simple.
"""
x = 23.0
a = random.uniform(0.0, 100.0*x)
i = 0
thing = False

while thing==False:
	print a
	d = x-math.sqrt(a)
	a = a + d
	if d==0:
		thing = True
	else:
		thing = False
