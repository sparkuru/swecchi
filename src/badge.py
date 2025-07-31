# -*- coding: utf-8 -*-

'''
app: badge
author: shiguma
repo: https://github.com/shi9uma/swecchi.git
description: 徽章！
'''

import tools
import time

@tools.某科学的
def test(times):
    res = 0
    for x in range(5):
        res += times ** times
    return res

t1 = time.time()
test(1000)
print(time.time() - t1)