#! /usr/bin/python3
# TMHI-info.10m.py
# <xbar.title>TMHI Metrics</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>wine-geek</xbar.author>
# <xbar.author.github>roger-richards</xbar.author.github>
# <xbar.desc>Show TMHI Service Metrics</xbar.desc>
# <xbar.dependencies>python3, request </xbar.dependencies>
# <swiftbar.hideRunInTerminal>false</swiftbar.hideRunInTerminal>
# <swiftbar.refresh>True</swiftbar.refresh>

#Gets metrics from local T-Mobile Arcadyan gateway
#shows 4g & 5g bands, signal ⑇ bars, and a few metrics

import urllib.request
import json
from datetime import datetime

modem_url = ("http://192.168.12.1/TMI/v1/gateway?get=all")
newline = '\n'
DIVIDER = '---\n'

with urllib.request.urlopen(modem_url) as url:
    jdata = json.loads(url.read())

mtime = datetime.fromtimestamp(int(jdata['time']['localTime']))
localtime = mtime.strftime("%M:%S")

print('🟪')
print(DIVIDER)

print(jdata['device']['model'] + " ver " + jdata['device']['softwareVersion'] +" "+ jdata['device']['updateState']
      +"  --:"+ str(localtime))
band = '4g'
print(band + str(jdata['signal'][band]['bands']) + "⑇" + str(jdata['signal'][band]['bars'])
      + " /RSSI>-70: " + str(jdata['signal'][band]['rssi']) + " /SINR>1: " + str(jdata['signal'][band]['sinr'])
      + " /RSRP>-90: " + str(jdata['signal'][band]['rsrp']) +'| color=brown')
band = '5g'
print(band + str(jdata['signal'][band]['bands']) + "⑇" + str(jdata['signal'][band]['bars'])
      + " /RSSI>-70: " + str(jdata['signal'][band]['rssi']) + " /SINR>1: " + str(jdata['signal'][band]['sinr'])
      + " /RSRP>-90: " + str(jdata['signal'][band]['rsrp']) +'| color=green')
