import os
from cloudstackapi.cloud_stack import CloudStack

api_url = os.getenv('CPAPI')
apiKey  = os.getenv('CPAPIKEY')
secret  = os.getenv('CPSKEY')
 
api = CloudStack(api_url, apiKey, secret)

request = {  'serviceofferingid':'5a5a6fae-73db-44d6-a05e-822ed5bd0548', 
                  'templateid': '6e94d4d0-a1d6-405c-b226-e1ce6858c97d', 
                  'zoneid': 'c70c584b-4525-4399-9918-fff690489036',
                  'networkids': '250b249b-5eb0-476a-b892-c6a6ced45aad',
                  'projectid': '0be19820-1fe2-45ea-844e-77f17e16add5'
                }

requestvm = {'projectid': '0be19820-1fe2-45ea-844e-77f17e16add5'}


result = api.listVirtualMachines(requestvm)

for virtualmachine in result['virtualmachine']:

	requestvm = {'projectid': '0be19820-1fe2-45ea-844e-77f17e16add5', 'id': '%s' % (virtualmachine['id'])}
		
	print "\n","virtualmachine id: %s" % (virtualmachine['id'])
	print "virtualmachine name: %s" % (virtualmachine['name'])

	requestvm = {'id':'%s' % (virtualmachine['id']) }
	
	if virtualmachine['id'] != '4ce246f1-26a9-4646-95e4-9a3b0cb07b7a':
		print virtualmachine['name']
		print "Destroying: %s" % (virtualmachine['id'])

		result = api.destroyVirtualMachine(requestvm)

	# jobid = result['jobid']
	# loop =True
	# while loop:
	# 	result = api.queryAsyncJobResult({'jobid': '%s' % (jobid)})
	# 	if result['jobstatus']==1:
			
	# 		loop=False
	# 		request = {'projectid': '0be19820-1fe2-45ea-844e-77f17e16add5','virtualmachineid':'%s' % (virtualmachine['id'] ) }
	# 		result = api.listVolumes(request)
		
	# 		if result['volume']:
	# 			for volume in result['volume']:
	# 				requestvl = {'id': '%s' % (volume['id'])}
	# 				print "Destroying volume: %s" % (volume['id'])
	# 				result = api.deleteVolume(requestvl)
	# 				print result
