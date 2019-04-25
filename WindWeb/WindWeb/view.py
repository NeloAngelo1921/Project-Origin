# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from netCDF4 import Dataset
import numpy as np
import json
np.set_printoptions(precision = 2, threshold = 1e6, suppress = True)

def wind(request):
	data = getWindData('F:/NCEP/MON/uwnd.mon.1981-2010.ltm.nc', 'F:/NCEP/MON/vwnd.mon.1981-2010.ltm.nc')
	result = "success_jsonpCallback(" + data + ")"
	return HttpResponse(result)

def getWindData(upath, vpath):
 	ua = Dataset(upath)
 	va = Dataset(vpath)
 	print(ua.variables['lon'][:])
 	print(ua.variables['lat'][:])
 	udata = ua.variables['uwnd'][:]
 	vdata = va.variables['vwnd'][:]
 	wind = {}
 	wind['uData'] = np.ma.filled(udata).tolist()[0][0]
 	wind['vData'] = np.ma.filled(vdata).tolist()[0][0]
 	ua.close()
 	va.close()
 	return json.dumps(wind)