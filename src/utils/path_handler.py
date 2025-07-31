# -*- coding: utf-8 -*-

'''
app: utils.decorator
author: shiguma
repo: https://github.com/shi9uma/swecchi.git
description: 目录操作函数
'''

# imports
import os

# self
import utils.telescope as telescope

# functions


def dirname(path: str) -> str:
    '''
    wrapper for os.path.dirname(path)
    '''
    return os.path.dirname(path)


def get_root_path() -> str:
    '''
    获取整个项目的根目录
    '''
    return dirname(dirname(dirname(os.path.realpath(__file__))))


def 检查传入路径是否存在(path: str) -> bool:
    '''
    检查传入路径是否存在
    '''
    return os.path.exists(path)


def 检查传入路径是文件还是文件夹(path: str) -> int:
    '''
    检查传入的路径是文件还是文件夹
    '''
    if os.path.isfile(path):
        return 1
    if os.path.isdir(path):
        return 2
    return 0


def 处理传入的文件夹路径(path: str) -> str:
    '''
    处理传入的文件夹路径, 如果不存在则创建, 如果已存在但不是文件夹则创建一个 _dir 标识的文件夹
    '''
    flag = 检查传入路径是文件还是文件夹(path)
    if flag == 1:
        path = '{}_dir'.format(path)
    elif flag == 2:
        return path
    try:
        os.makedirs(path)
    except BaseException as e:
        print(e)
    finally:
        return path


def xpath(*args: str) -> str:
    '''
    去掉双斜杠, 多个传入则自动拼接
    '''
    def _去掉双斜杠(path: str):
        return path.replace('\\', '/').replace('\\\\', '/')

    if len(args) > 1:
        base_path = args[0]
        telescope.看一下有没有非法元素(args, str)
        for _path in args[1:]:
            base_path = os.path.join(base_path, str(_path))
        return _去掉双斜杠(base_path)
    return _去掉双斜杠(args[0])
