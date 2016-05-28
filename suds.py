# -*- coding: utf-8 -*-
import sys

from suds.client import Client

url = 'http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl'
client = Client(url)
asc = client.service.getCountryCityByIp(sys.argv[1])
print asc.string[0]+','+asc.string[1]
