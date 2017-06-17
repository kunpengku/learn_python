#coding:utf8

from enum import Enum

class Channel(Enum):
    """推送平台"""

    gcm = 0
    getui = 1
    jpush = 2




print Channel

c = 'jpush'
n_c = getattr(Channel, c)
print n_c == Channel.gcm


#getattr 有 反射的感觉
