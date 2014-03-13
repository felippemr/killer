import os
from cloudstackapi.cloud_stack import CloudStack

api_url = os.getenv('CPAPI')
apiKey  = os.getenv('CPAPIKEY')
secret  = os.getenv('CPSKEY')
 
api = CloudStack(api_url, apiKey, secret)
 
request = {'listall': 'true'}
result = api.listVirtualMachines(request)
print "count", result['count']
print "api url", api.value