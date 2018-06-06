#calculate total available host name in "GlOBAl" region

import json
import pdb
import collections

#funct() to convert Unicode to str
def unicodeTostr(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(unicodeTostr, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(unicodeTostr, data))
    else:
        return data

f = open("ip-ranges.json")
data1 = json.load(f)

data = unicodeTostr(data1)
#print data
#print type(data)
f.close()
#type(data)



#return index value of '/' from ip_prefix to calculate netmask_length
def find_prefix(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            return i+1
    

for major, subdict in data.iteritems():
   # print(major)
    #print(subdict)
    for item in subdict:
        #print item
        if "GLOBAL" in item.itervalues():
            num_hosts= ""
            prefix = ""
            prefix = item['ip_prefix']
            print("ip_prefix: %s" %(prefix))
            index=find_prefix(prefix, '/')  
            #calculate netmask_length 
            prefix1 =  prefix[index:] 
            print("netmask_length: %s" %(prefix1))
            #coverted unicode into string if any
            encodedstr = prefix1.encode("utf-8")
           # pdb.set_trace()
            host = 2**(32 - int(encodedstr))-2    
            print("number of available host for given prefix: %d" %(host))