import math

for a in range(1,1001):
	for b in range(a,1001):
		if a + b + math.sqrt(a**2 + b**2) == 1000:
			print(a*b*math.sqrt(a**2 + b**2))
		else:
			...
