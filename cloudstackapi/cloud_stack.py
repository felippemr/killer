import hashlib, hmac, string, base64, urllib
import json, urllib
from base_api_call import BaseApiCall

class CloudStack(BaseApiCall):
    def __getattr__(self, name):
        def handlerFunction(*args, **kwargs):
            action = args[0] 
            if kwargs:
                return self._make_request(name, kwargs)
            return self._make_request(name, args[1], action)
        return handlerFunction
 
    def _http_get(self, url):
        response = urllib.urlopen(url)
        return response.read()

    def _http_post(self, url, data):
        response = urllib.urlopen(url,data)
        return response.read()
 
    def _make_request(self, command, args, action):
        args['response'] = 'json'
        args['command'] = command
        self.request(args,action)
        if action == 'GET':
            data = self._http_get(self.value)
        else:
            data = self._http_post(self.value, self.query)
        # The response is of the format {commandresponse: actual-data}
        key = command.lower() + "response"
        return json.loads(data)[key]
