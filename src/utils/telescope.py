# -*- coding: utf-8 -*-

'''
app: utils.telescope
author: shiguma
repo: https://github.com/shi9uma/swecchi.git
description: 各种查看函数
'''


def 色色(text: str = '', color: int = 1) -> str:
    '''
    返回对应的控制台 ANSI 颜色
    '''
    color_table = {
        0: '\033[1;30m{}\033[0m',   # 黑色加粗
        1: '\033[1;31m{}\033[0m',   # 红色加粗
        2: '\033[1;32m{}\033[0m',   # 绿色加粗
        3: '\033[1;33m{}\033[0m',   # 黄色加粗
        4: '\033[1;34m{}\033[0m',   # 蓝色加粗
        5: '\033[1;35m{}\033[0m',   # 紫色加粗
        6: '\033[1;36m{}\033[0m',   # 青色加粗
        7: '\033[1;37m{}\033[0m',   # 白色加粗
    }
    return color_table[color].format(text)


def 看一下有没有非法元素(_组合类型, _合法元素类型):
    '''
    查看传入的组合有没有指定以外的非法元素
    '''
    for _茵蒂克丝 in range(len(_组合类型)):
        if not isinstance(_组合类型[_茵蒂克丝], _合法元素类型):
            print('茵蒂克丝：{}，传入值：{}，传入类型：{}，期望类型：{}'.format(
                色色(_茵蒂克丝, 1), 色色(_组合类型[_茵蒂克丝], 2), 色色(type(_组合类型[_茵蒂克丝]), 3), 色色(_合法元素类型, 4)))


def get_dict_dict(dict_obj: dict) -> dict:
    '''
    以字典形式展示字典中各个值
    '''
    dict_obj_container = dict()
    for key, value in dict_obj.items():
        dict_obj_container[key] = value
    return dict_obj_container


def get_dict_list(dict_obj: dict) -> list:
    '''
    以列表形式展示字典中各个值    
    '''
    dict_obj_container = list()
    for key, value in dict_obj.items():
        dict_obj_container.append([key, value])
    return dict_obj_container


def get_class_attr(class_obj: object) -> dict:
    '''
    以字典形式展示类中各个属性
    '''
    class_obj_attrs = [attr for attr in dir(
        class_obj) if not attr.startswith('__')]
    class_obj_container = dict()
    for attr in class_obj_attrs:
        class_obj_container[attr] = getattr(class_obj, attr)
    return class_obj_container
