def build_staircase(x, y):
	a = ["_"]
	count = x-1
	p = []
	l = []
	for i in range(x+1):
		p.append(list(y*i))
	p.remove([])
	for i in range(len(p)):
		l.append(p[i]+a*count)
		count = count - 1

	return['\n'.join(map(str, l))]

print(build_staircase(3, '#'))