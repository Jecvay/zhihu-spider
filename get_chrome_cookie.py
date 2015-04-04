__author__ = 'Jecvay'

"""
    从 Windows 下的 chrome 获取 cookies 记录
"""

import sqlite3
import win32crypt
import os


def get_chrome_cookie(url, path='"C:\\Users\\Liu\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"'):
    cmd = 'copy ' + path + ' D:\\python-chrome-cookies'
    print(cmd)
    os.system(cmd)
    conn = sqlite3.connect("d:\\python-chrome-cookies")
    ret_list = []
    ret_dict = {}
    for row in conn.execute("SELECT host_key, name, path, value, encrypted_value FROM cookies"):
        if row[0] != url:
            continue
        ret = win32crypt.CryptUnprotectData(row[4], None, None, None, 0)
        ret_list.append((row[1], ret[1]))
        ret_dict[row[1]] = ret[1].decode()
    conn.close()
    os.system('del "D:\\python-chrome-cookies"')
    return ret_dict