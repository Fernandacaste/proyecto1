def prob_1 (n):
	if n%2 == 0:
		return True
	else:
		return False
def prob_2 (n):
	return 5/9*(n-32)
def prob_3 (n,m):
	return n**m
def prob_4 (n,palabra):
	cas = (n-len(palabra))//2
	cas2= n-(cas+len(palabra))
	return "*"*cas+palabra+"*"*cas2
def prob_5 