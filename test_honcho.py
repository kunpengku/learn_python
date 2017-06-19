import time

for i in range(4):

    print i

import os

print os.environ['FOO_BOO']


import envcfg.json.asset as config

print config
print dir(config)
print config.ROOT



