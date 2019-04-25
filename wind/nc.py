# -*- conding: UTF-8 -*-
# 获取风场数据

from netCDF4 import Dataset
import numpy as np


def getWindData(upath, vpath):

    np.set_printoptions(precision = 2, threshold = 100000000, suppress = True)

    ua = Dataset(upath, 'r')
    va = Dataset(vpath, 'r')
    udata = ua.variables['u500'][:]
    vdata = va.variables['v500'][:]
    print(udata[0][0][0][0])
    #print(np.ma.filled(udata))
    wind = {'sLon':0, 'sLat':-90, 'interval': 2.5}
    print(type(np.ma.filled(udata)[0][0]))
    wind['uData'] = udata
    wind['vData'] = vdata
    ua.close()
    va.close()

if __name__ == "__main__":
    up = 'F:/CFSv2/day/u500.20190423.day.nc'
    vp = 'F:/CFSv2/day/v500.20190423.day.nc'
    getWindData(up, vp)