#!/usr/bin/python
# coding:utf-8

"""
@author: Shiying
@software: PyCharm
@file: XXX.py
@time: 2019/XX/XX XX:XX
"""

import execjs

js = execjs.compile(open(r'test.js').read())
zz = '55e0aHRVhJYAS0cDovL212dmlkZW8xMC5tZWl0dWRhdGEuY29tLzVkMzNmMGRmM2RkYzRwMm5sd3N0cWg3OTA2X0gyNjRfMV85YzNiM2QwOTNhMWRhNS5tcDQ/az1kODlkOTVmZmRlNWZjNzQ0YzUwOTY0NDZiZjNhNTE0OCZ0PTVkNDEIQbtCanOZiOWY4'
print(js.call("main", zz))



def decode(target):
    """
    执行 js 的解码函数
    :param target:
    :return: 解码后的结果
    """
    js = execjs.compile(open(r'./test.js').read())
    resualt = js.call("main", target)
    return resualt