

import more_itertools


apples = [1,2,3,4,5,6,7,8,9,10]

# 将一个大的list ，根据参数，拆成N个小一些的list
for apple in more_itertools.chunked(apples, 4):

    print apple



# pip install more_itertools
