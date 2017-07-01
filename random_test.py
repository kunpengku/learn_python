import random
import time

def make_random_nonce():
    large_number = random.randrange(1e6, 1e8)
    print large_number
    print 1e6
    print 1e8
    return '%X' % (int(time.time()) ^ large_number)


print make_random_nonce()

