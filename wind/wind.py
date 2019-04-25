# -*- conding: UTF-8 -*-

class wind:
    def __init__(self, lon, lat, u, v):
        '''
        构造方法初始化
        lon: 经度
        lat: 纬度
        u: u向风风速
        v: v向风风速
        '''
        self.lon = lon
        self.lat = lat
        self.u = u
        self.v = v
    
    def __str__(self):
        '''
        重写str方法 输出需要的值
        '''
        return "'lon':{},'lat':{},'u':{},'v':{}".format(self.lon, self.lat, self.u, self.v)