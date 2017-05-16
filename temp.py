import GA
import random


sample = [ random.randint(1, 13) for i in range(1,80) ]

print sample

u = GA.evalOneMax(sample)

print u