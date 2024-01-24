import urllib
from urllib import request

# for module in dir(urllib):
#   print(module)

resp = request.urlopen("https://www.wikipedia.org")
print(type(resp))

print(resp.code)  # prints response code
print(resp.length)
print(resp.peek())  # show a small portion
data = resp.read()
print(type(data))
print(len(data))

# decoding
html = data.decode("UTF-8")
print(type(html))  # type is not a string
print(html)
print(resp.read())  # prints nothing because
print(resp.isclosed())  # connection has been closed by python
