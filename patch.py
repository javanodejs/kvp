# coding: utf8

from hashlib import md5
import time
import json
from urllib import request


appid = 'wxa2c324b63b2a9e5e'
secret = '9190a38214f454332431f0604b6b5b8d'
# macbinn
openid = 'oc6rl5eyyaIml3ONiLvECjWigYps'
# openid = 'oc6rl5U0qqWx1y6uLE6LPMT6dofw'


def md5_hash(s):
    m = md5()
    m.update(s.encode('utf8'))
    return m.hexdigest()


def sign(data, ts=None):
    data['time'] = int(time.time()) if ts is None else ts
    data['openid'] = openid
    data['wx_appid'] = appid
    data['wx_secret'] = secret
    sorted_keys = sorted(data.keys())
    s = ''
    for key in sorted_keys:
        s += key + '=' + str(data[key]) + '&'
    del data['wx_appid']
    del data['wx_secret']
    data['sign'] = md5_hash(s[:-1])
    return data


def upload_record(record):
    data = {
        'plat': 'wx',
        'v': 1,
        'record': record,
    }
    signed = sign(data)
    data = json.dumps(signed).encode('utf8')

    headers = {
        'Host': 'wxwyjh.chiji-h5.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.4(0x17000428) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wxa2c324b63b2a9e5e/65/page-frame.html',
        'Accept-Language': 'zh-cn',
    }

    req = request.Request('https://wxwyjh.chiji-h5.com/api/archive/upload',
                          headers=headers, data=data)

    r = request.urlopen(req)
    print(r.code)
    print(r.info())
    print(r.read())


def main():
    record = {
        "v": "bJ-JjgTBwkyZvxyHb2s9hgy-eiu2oyeRwByTjTGG",
        "uid": "oc6rl5eyyaIml3ONiLvECjWigYps",
        "isPingJiaed": False,
        "isSoundOff": True,
        "isShackOff":True,
        "GMTimeG": 1560224899601,
        "GMTimeP": -1,
        "shareTime": -1,
        "level": 1314,
        "levelMax": 1314,
        "lDamage": 1280,
        "lCount": 360,
        "lJiaZhi": 1,
        "lRiChang": 1,
        "curFu": 6,
        "levelFuCount": [36, 36, 36, 36, 36, 36, 36, 36, 36, 36],
        "levelFuDamage": [1280, 1280, 1280, 1280, 1280, 1280, 1280, 1280, 1280, 1280],
        "getTime": "",
        "bgIndex": 3,
        "bgmIndex": 3,
        "money": "900000000",
        "tipFU": False,
        "G1": False,
        "G2": False,
        "G3": False,
        "tiLi": 75,
        "tiLiBackTime": 1560659599603,
        "today": 16,
        "playCount": 5,
        "shareCount": 2,
        "videoCount": 5,
        "isGuanZhu": 0,
        "isShouCang": True,
        "tryFuCount": 0,
        "pos": "湖北,武汉",
        "posUpdate": 15,
        "zuanShi": 0,
        "teQuanTime": -1,
        "isTeQuaned": False,
        "jiFenId": [""],
        "getTime2": 1560655780373,
        "teQuanShowed": False,
        "teQuanGetTime": 1558327385276,
        "loginTime": 0,
        "EM_isFirst1": False,
        "EM_score": 0,
        "EM_roundBestTime": 122,
        "EM_localRank": 20,
        "EM_refreshRankTime": 1560700799200,
        "mode": 1,
        "wjCount": 2,
        "signin_Count": 2,
        "signin_Time": 1560700799538,
        "signin_Type": 2,
        "s": "32e37243cc6458e1cdb4aba98825e125",
    }
    record_s = json.dumps(record)
    upload_record(record_s)


if __name__ == '__main__':
    main()

