from urllib import request, parse, error
"""
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)


with request.urlopen('http://python.org') as response:
    html = response.read().decode()
print(html)

req = request.Request('http://python.org/')
with request.urlopen(req) as response:
    thisPage = response.read()
print(thisPage)
"""

url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python'}
data = parse.urlencode(values)
data = data.encode('ascii')
print(data)