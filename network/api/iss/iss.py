# API Request example in Python

import urllib.request
import json
from datetime import datetime

req = urllib.request.Request('http://api.open-notify.org/iss-pass.json?lat=44.6134227&lon=1.1366893')
res = urllib.request.urlopen(req)
page = res.read()
api = json.loads(page)

if api['message'] == 'success':

    for issRes in api['response']:
        
        issDur = str(int(issRes['duration']) // 60) + ' minutes'
        issTime = datetime.fromtimestamp(issRes['risetime'])
        
        ret = '''
            Duration: {}\n
            Date: {}\n
            ==========================
        '''.format(issDur, issTime)
        
        print(ret)
