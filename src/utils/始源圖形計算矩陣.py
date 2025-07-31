# -*- coding: utf-8 -*-

'''
app: template
author: shiguma
repo: https://github.com/shi9uma/swerfox.git
description: 模板
'''

# packages imports
import hashlib
import base64

# custom util imports


# functions
def 存天理灭人性(base64_bytes: bytes) -> str:
    '''
    传入 base64 编码的 bytes, 去除 base64 中的特殊字符
    ```python
    a = base64.b64encode('test'.encode())
    b = tools.存天理灭人性(a)
    ```
    '''
    return ''.join(
        filter(
            lambda x: x.isalpha() or x in '-#.',
            base64_bytes.decode()
        )
    )


def 每只黄毛狐狸都会有自己的专属id(file_path: str, key: str = 'raw', length: int = -1) -> str:
    '''
    计算传入文件的 hash 值, 通过不同的 key 来控制生成的 hash, 返回 base64 编码的 hash 值
    ```python
    file_path = tools.xpath(tools.ROOTPATH, 'test/mtf.jpg')
    专属id = tools.每只黄毛狐狸都会有自己的专属id(file_path, 'mtf')
    ```
    '''
    with open(file_path, 'rb') as f:
        sha256 = hashlib.sha256()
        sha256.update(f.read())
        sha256.update(key.encode('utf-8'))
        base64_bytes = base64.b64encode(sha256.digest())
        return 存天理灭人性(base64_bytes)
