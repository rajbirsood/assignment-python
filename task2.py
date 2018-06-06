#print totals by region and service

import json
import pdb
import collections
from collections import OrderedDict

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

#define global variables
GLOBAL=0
TOTAL=0
useast1=0
useast2=0
uswest1=0
uswest2=0
saeast1=0
cacentral1=0
eucentral1=0
euwest1=0
euwest2=0
euwest3=0
apnortheast1=0
apnortheast2=0
apnortheast3=0
EC2=0
CLOUDFRONT=0
S3=0
ROUTE53_HEALTHCHECKS=0
AMAZON=0
CLOUD9=0
AMAZON_CONNECT=0
CODEBUILD=0
CLOUDFRONT=0
ROUTE53=0

f = open("ip-ranges.json")
data1 = json.load(f)
data = unicodeTostr(data1)
#print type(data)
f.close()
#type(data)

#return index value of '/' from ip_prefix to calculate netmask_length
def find_prefix(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            return i+1

def find_host(item):
    num_hosts= ""
    prefix = ""
    host_no = 0
    prefix = item['ip_prefix']
   # print("ip_prefix: %s" %(prefix))
    index=find_prefix(prefix, '/')  
    #calculate netmask_length 
    prefix1 =  prefix[index:] 
    #print("netmask_length: %s" %(prefix1))
    #coverted unicode into string
    encodedstr = prefix1.encode("utf-8")
     # pdb.set_trace()
    host_no = (2**(32 - int(encodedstr))-2) 
   # print("number of available host for given prefix: %d" %(host_no))
    return host_no
 
    

for major, subdict in data.iteritems():
    #print(major)
    #print(subdict)
    total = 0;
   # host = ""
    for item in subdict:
        #print item
       
        if "GLOBAL" in item.itervalues():
            host = find_host(item) 
            GLOBAL = GLOBAL+host
            TOTAL = TOTAL+host
            
        
        elif "us-west-2" in item.itervalues():
            host = find_host(item)
            uswest2=uswest2+host
            TOTAL = TOTAL+host
           
        elif "sa-east-1" in item.itervalues():
            host = find_host(item)
            saeast1=saeast1+host
            TOTAL = TOTAL+host
          
        elif "ca-central-1" in item.itervalues():
            host = find_host(item)
            cacentral1=cacentral1+host
            TOTAL = TOTAL+host
            
        elif "eu-central-1" in item.itervalues():
            host = find_host(item)
            eucentral1=eucentral1+host
            TOTAL = TOTAL+host
            
        elif "us-east-1" in item.itervalues():
            host = find_host(item)
            useast1=useast1+host
            TOTAL = TOTAL+host
             
        elif "us-east-2" in item.itervalues():
            host = find_host(item)
            useast2=useast2+host
            TOTAL = TOTAL+host
            
        elif "sa-east-1" in item.itervalues():
            host = find_host(item)
            saeast1=saeast1+host
            TOTAL = TOTAL+host
           
        elif "us-west-1" in item.itervalues():
            host = find_host(item)
            uswest1=uswest1+host
            TOTAL = TOTAL+host
           
        elif "eu-west-1" in item.itervalues():
            host = find_host(item)
            euwest1=euwest1+host
            TOTAL = TOTAL+host
           
        elif "eu-west-2" in item.itervalues():
            host = find_host(item)
            euwest2=euwest2+host
            TOTAL = TOTAL+host
         
        elif "eu-west-3" in item.itervalues():
            host = find_host(item)
            euwest3=euwest3+host
            TOTAL = TOTAL+host
          
        elif "ap-northeast-1" in item.itervalues():
            host = find_host(item)
            apnortheast1=apnortheast1+host
            TOTAL = TOTAL+host
        elif "ap-northeast-2" in item.itervalues():
            host = find_host(item)
            apnortheast2=apnortheast2+host
            TOTAL = TOTAL+host
        elif "ap-northeast-3" in item.itervalues():
            host = find_host(item)
            apnortheast3=apnortheast3+host
            TOTAL = TOTAL+host
        elif "CLOUDFRONT" in item.itervalues():
            host = find_host(item)
            CLOUDFRONT=CLOUDFRONT+host
            TOTAL = TOTAL+host
        elif "ROUTE53" in item.itervalues():
            host = find_host(item)
            print("route 53 :%d %(host)")
            ROUTE53=ROUTE53+host
            TOTAL = TOTAL+host
        elif "CODEBUILD" in item.itervalues():
            host = find_host(item)
            CODEBUILD=CODEBUILD+host
            TOTAL = TOTAL+host 
        elif "AMAZON_CONNECT" in item.itervalues():
            host = find_host(item)
            AMAZON_CONNECT=AMAZON_CONNECT+host
            TOTAL = TOTAL+host
        elif "CLOUD9" in item.itervalues():
            host = find_host(item)
            CLOUD9=CLOUD9+host
            TOTAL = TOTAL+host
        elif "AMAZON" in item.itervalues():
            host = find_host(item)
            AMAZON=AMAZON+host
            TOTAL = TOTAL+host
        elif "ROUTE53_HEALTHCHECKS" in item.itervalues():
            host = find_host(item)
            ROUTE53_HEALTHCHECKS=ROUTE53_HEALTHCHECKS+host
            TOTAL = TOTAL+host
        elif "S3" in item.itervalues():
            host = find_host(item)
            S3=S3+host
            TOTAL = TOTAL+host
        elif "CLOUDFRONT" in item.itervalues():
            host = find_host(item)
            CLOUDFRONT=CLOUDFRONT+host
            TOTAL = TOTAL+host
        elif "EC2" in item.itervalues():
            host = find_host(item)
            EC2=EC2+host
            TOTAL = TOTAL+host
        else:
            host = find_host(item)
            TOTAL = TOTAL+host
            
            
  
            
    
    
    
    
    d = {'TOTAL':TOTAL,
           'Regions':{'Global':GLOBAL,
                     'us-east-1':useast1,
                     'us-east-2': useast2,
                     'us-west-1' : uswest1,
                     'us-west-2':uswest2,
                     'ca-central-1': cacentral1,
                     'eu-central-1': eucentral1,
                     'eu-west-1':euwest1,
                      'eu-west-2':euwest2,
                     'eu-west-3': euwest3,
                     'ap-northeast-1': apnortheast1,
                     'ap-northeast-2': apnortheast2,
                     'ap-northeast-3': apnortheast3,
                    },
          'Services':{
                      'EC2' : EC2,
                      'CLOUDFRONT': CLOUDFRONT,
                       'S3' : S3,
                       'ROUTE53_HEALTHCHECKS' : ROUTE53_HEALTHCHECKS,
                       'AMAZON' : AMAZON,
                       'CLOUD9' : CLOUD9,
                       'AMAZON_CONNECT' : AMAZON_CONNECT,
                        'CODEBUILD' : CODEBUILD,
                       'CLOUDFRONT' : CLOUDFRONT,
                        'ROUTE53' : ROUTE53,
              
          }
        }  
    
    print(d)
    
    print('\n')
    
    print("Total : %d" %(TOTAL))    
    print("Global : %d" %(GLOBAL))
    print("us-east-1: %d" %(useast1))
    print("us-east-2 : %d" %(useast2))
    print("us-west-1 : %d" %(uswest1))
    print("us-west-2: %d" %(uswest2))
    print("ca-central-1: %d" %(cacentral1))
    print("eu-central-1: %d" %(eucentral1))
    print("eu-west-1: %d" %(euwest1))
    print("eu-west-2: %d" %(euwest2))
    print("eu-west-3: %d" %(euwest3))
    print("ap-northeast-1: %d" %(apnortheast1))
    print("ap-northeast-2: %d" %(apnortheast2))
    print("ap-northeast-3: %d" %(apnortheast3))
    
    print("EC2 : %d" %(EC2))
    print("CLOUDFRONT : %d" %(CLOUDFRONT))
    print("S3 : %d" %(S3))
    print("ROUTE53_HEALTHCHECKS : %d" %(ROUTE53_HEALTHCHECKS))
    print("AMAZON : %d" %(AMAZON))
    print("CLOUD9 : %d" %(CLOUD9))
    print("AMAZON_CONNECT : %d" %(AMAZON_CONNECT))
    print("CODEBUILD : %d" %(CODEBUILD))
    print("CLOUDFRONT : %d" %(CLOUDFRONT))
    print("ROUTE53 : %d" %(ROUTE53))
        