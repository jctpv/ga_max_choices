import random

lc=[]
for i in range(0,62):
    lc.append(random.sample(range(1, 13), 3))

print lc

sample = [ random.randint(1, 13) for i in range(1,80) ]

print sample