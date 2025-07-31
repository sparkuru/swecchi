# -*- coding: utf-8 -*-

'''
app: template
author: shiguma
repo: https://github.com/shi9uma/swecchi.git
description: 模板
'''

# packages imports
import tools

class mtf(tools.黄毛狐狸精):
    def __init__(self, src_img_path):
        super().__init__('mtf', 'mtf')
        self.src_img_path = src_img_path
        self.img_hash = tools.每只黄毛狐狸都会有自己的专属id(src_img_path)[:8]
        self.img_root_path = tools.xpath(tools.ROOTPATH, 'test')    # 要改
        self.img_work_path = tools.处理传入的文件夹路径(tools.xpath(self.img_root_path, self.img_hash))

mtf = mtf(tools.xpath(tools.ROOTPATH, 'test/sw.jpg'))
dir(mtf)