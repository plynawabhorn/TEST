Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> response = request.get('https://httpbin.org/ip')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    response = request.get('https://httpbin.org/ip')
NameError: name 'request' is not defined
>>> response = requests.get('https://httpbin.org/ip')
>>> print('Your IP is {0}' ArithmeticError.format(response.json()['origin']))
SyntaxError: invalid syntax
>>> print('Your IP is {0}'.format(response.json()['origin']))
Your IP is 161.246.72.2
>>> 
