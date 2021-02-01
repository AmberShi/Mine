#!/usr/bin/python
# coding:utf-8

"""
@author: Shiying
@software: PyCharm
@file: sign
@time: 2021/1/30 17:30
"""

#!/usr/bin/python
# coding:utf-8

import datetime

import requests



def zhanzhangtuku_sign():
    # 站长图库签到
    url = 'https://www.zztuku.com/user-signin.html'
    headers = {
        'cookie': '__gads=ID=e4fa67b36c3d0840-22b450e687c5007d:T=1609761155:RT=1609761155:S=ALNI_MZaWP3FTwJ-atJrUvB4Vth8oUSCzw;tk_user_id=0pGP6O;Hm_lvt_36d091ca4167858e40c7bf39f954e3f9=1609761154,1609761176;Hm_lpvt_36d091ca4167858e40c7bf39f954e3f9=1609761176',
        'user-agent': 'Mozilla/5.0(WindowsNT6.1;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/87.0.4280.88Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.post(url=url,headers=headers)
    if response.status_code == 200:
        print(response.json())
        print(datetime.datetime.today().strftime('%Y-%m-%d'))
if __name__ == '__main__':
    zhanzhangtuku_sign()