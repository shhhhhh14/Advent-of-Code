
inp = [i.strip().split() for i in open('day4.txt', 'r').readlines()]

with open('day4.txt') as f:
    a = f.readlines()

p1 = 0
p2 = 0

for line in a:
    b = line.split()
    c = set(b)
    if len(b) == len(c):
        p1 += 1

for i in inp:
    if len(set(''.join(sorted(u)) for u in i)) == len(i):
        p2 += 1

print ("Part 1:", p1)
print ("Part 2:", p2)
