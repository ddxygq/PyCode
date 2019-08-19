import requests

url = 'http://www.ikeguang.com'
re = requests.get(url)
print(re.content.decode('utf-8'))

