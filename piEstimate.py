import random
def sample(p):
        x,y = random.random(), random.random()
        return 1 if x*x + y*y < 1 else 0

NUM_SAMPLES = 100
count = map(sample, xrange(0,NUM_SAMPLES))
print count
print reduce(lambda a, b: a + b, count)/float(NUM_SAMPLES)