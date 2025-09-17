import sys
n = 0
x = 0
y = 0
for line in sys.stdin:
    a = line.split()
    if a:
        n = int(a[0])
        x = int(a[1])
        y = int(a[2])
    break
num = 0
for i in range(1,n+1,1):
    
    if i%x == 0 or i%y == 0 or y%i == 0 or x%i == 0:
        num += 1
print(num)

