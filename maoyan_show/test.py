from pickle import dumps, loads
import json
import redis
r = redis.Redis(host='10.11.56.94',port=6379,db=0,decode_responses=True)
data_list = r.lrange('maoyan:items',0,-1)
# print(json.loads(str(data_list)))
data_dict = {}
for data in data_list:
    loads_dict = json.loads(data)
    data_dict[loads_dict['rank']] = loads_dict
data_dict = sorted(data_dict.items(),key=lambda x:int(x[0]))
print(data_dict)