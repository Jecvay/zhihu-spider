__author__ = 'Jecvay'

import requests

from get_chrome_cookie import get_chrome_cookie
import application

if __name__ == '__main__':
    ck = get_chrome_cookie(application.settings['domain'])
    x = requests.get(application.settings['url'], cookies=ck)
    print(x.text)

