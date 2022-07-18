#!/usr/bin/python

import json
import time

with open('/Users/wh/Downloads/json.txt', 'r') as f:    
    jsonStr = f.read(65535)
    obj = json.loads(jsonStr)
    for x in obj:
        orderId = x['_source']['orderId']
        createTime = x['_source']['createTime']
        createTime = createTime.replace('+08:00', '')
        # //"2022-07-15T20:00:25+08:00"
        seconds = time.mktime(time.strptime(createTime,"%Y-%m-%dT%H:%M:%S"))
        print("UPDATE roll_order set collect_time = %d WHERE id = %s;" % (seconds, orderId))
