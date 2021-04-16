def divisors(n): 
	list = []
	for i in range(n+1): 
		if n % i == 0: 
			list.append(i)
	return list