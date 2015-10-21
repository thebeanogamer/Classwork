a = ["Jamie", "George", "Fred", "Sue"]
b = [4,76,24,87]
n = 0
t = 0
x = 0

while x < len(a):
	n = n + len(a[x])
	x = x + 1

x = 0
while x < len(b):
	t = t + b[x]
	x = x + 1

t = t * 4
z = t + n

print(z, "bytes!")
