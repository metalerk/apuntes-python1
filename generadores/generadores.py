def getNumbers(n):
	for x in range(n):
		yield x

for x in getNumbers(10):
	print(x)

l = getNumbers(10)
print(l)
val = l.next()
print(val)
val = l.next()
print(val)
val = l.next()
print(val)
val = l.next()
print(val)
val = l.next()
print(val)
val = l.next()
print(val)
