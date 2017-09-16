import requests
r = request.get('https://api.github.com')
r = requests.post('http://httpbin.org/post')
r = requests.put('http://httpbin.org/put')
r = requests.delete('http://httpbin.org/delete')
r = request.head('http://httpbin.org/get')
r = request.options('http:/httpbin.org/get')

payload = {'key1':'value1','key2':'value2','key3':'value3'}
r = requests.get('http://httpbin.org/get',params=payload)
print(r.url)