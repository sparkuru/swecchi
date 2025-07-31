# -*- coding: utf-8 -*-

'''
app: tools
author: shiguma
repo: https://github.com/shi9uma/swerfox.git
description: utils tools 入口
'''

# packages imports
import sys
sys.path.append('.')

# custom util imports
import utils.始源圖形計算矩陣 as 始源圖形計算矩陣
import utils.telescope as telescope
import utils.template as template
import utils.decorator as decorator
import utils.path_handler as path_handler

# GLOBAL
ROOTPATH = path_handler.get_root_path()
CONFIGPATH = '{}/{}'.format(ROOTPATH, 'resources/config')

# homo
某科学的 = decorator.某科学的
class 黄毛狐狸精(template.template): pass

# path_handler
@decorator.观测之石
def dirname(path: str) -> str:
    '''
    wrapper for os.path.dirname(path)
    '''
    return path_handler.dirname(path)


@decorator.观测之石
def 检查传入路径是否存在(path: str) -> bool:
    '''
    检查传入路径是否存在
    '''
    return path_handler.检查传入路径是否存在(path)


@decorator.观测之石
def 检查传入路径是文件还是文件夹(path: str) -> int:
    '''
    检查传入的路径是文件还是文件夹
    '''
    return path_handler.检查传入路径是文件还是文件夹(path)


@decorator.观测之石
def 处理传入的文件夹路径(path: str) -> str:
    '''
    处理传入的文件夹路径, 如果不是则创建, 如果是则返回路径
    '''
    return path_handler.处理传入的文件夹路径(path)


@decorator.观测之石
def xpath(*args: str) -> str:
    '''
    去掉双斜杠, 多个传入则自动拼接
    '''
    return path_handler.xpath(*args)

# telescope
@decorator.观测之石
def 色色(text: str = '', color: int = 1) -> str:
    '''
    返回对应的控制台 ANSI 颜色
    '''
    return telescope.色色(text, color)


@decorator.观测之石
def get_dict_dict(dict_obj: dict) -> dict:
    '''
    以字典形式展示字典中各个值
    '''
    return telescope.get_dict_dict(dict_obj)


@decorator.观测之石
def get_dict_list(dict_obj: dict) -> list:
    '''
    以列表形式展示字典中各个值    
    '''
    return telescope.get_dict_list(dict_obj)


@decorator.观测之石
def get_class_attr(class_obj: object) -> dict:
    '''
    以字典形式展示类中各个属性
    '''
    return telescope.get_class_attr(class_obj)


@decorator.观测之石
def 看一下有没有非法元素(_组合类型, _合法元素类型):
    '''
    查看传入的组合有没有指定以外的非法元素
    '''
    return telescope.看一下有没有非法元素(_组合类型, _合法元素类型)

# 树状图设计者
@decorator.观测之石
def 存天理灭人性(base64_bytes: bytes) -> str:
    '''
    传入 base64 编码的 bytes, 去除 base64 中的特殊字符
    ```python
    a = base64.b64encode('test'.encode())
    b = tools.存天理灭人性(a)
    ```
    '''
    return 始源圖形計算矩陣.存天理灭人性(base64_bytes)


@decorator.观测之石
def 每只黄毛狐狸都会有自己的专属id(file_path: str, key: str = 'mtf') -> str:
    '''
    计算传入文件的 hash 值, 通过不同的 key 来控制生成的 hash, 返回 base64 编码的 hash 值
    ```python
    file_path = tools.xpath(tools.ROOTPATH, 'test/mtf.jpg')
    专属id = tools.每只黄毛狐狸都会有自己的专属id(file_path, 'mtf')
    ```
    '''
    return 始源圖形計算矩陣.每只黄毛狐狸都会有自己的专属id(file_path, key)
