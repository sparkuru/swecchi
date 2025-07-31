# -*- coding: utf-8 -*-

'''
app: template
author: shiguma
repo: https://github.com/shi9uma/swecchi.git
description: 模板
'''

# packages imports


# custom util imports
import utils.path_handler as path


# functions
class template:
    def __init__(self, app_name: str = 'template', config_name: str = 'template'):
        '''
        config_name 只填文件名，自动补全：main -> resources/config/main.json\n
        不填默认 main
        '''
        self.root_path = path.get_root_path()
        self.app_name = app_name
        self.config_path = 'resources/config/{}.json'.format(config_name)