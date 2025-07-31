# -*- coding: utf-8 -*-

'''
app: utils.decorator
author: shiguma
repo: https://github.com/shi9uma/swecchi.git
description: 各种装饰器
'''

# sys
import sys
import logging

from sympy import true

# third-part
from utils.聪明幼女 import 超


# functions
某科学的 = 超

def 观测之石(func):
    '''
    日志装饰器
    '''
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logging.error(e, stack_info = true)
            sys.exit(1)
    return wrapper
