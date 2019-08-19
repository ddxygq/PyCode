from bs4 import BeautifulSoup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="link1"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

# 创建beautifulsoup对象
soup = BeautifulSoup(html, 'html.parser')

# 打印soup内容
# print(soup.prettify())

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.get_text())

print(soup.body.contents)

print('==============')
# 通过标签名查找
print(soup.select('title')[0].text)
# 通过类名查找
print(soup.select('.sister')[0].text)
# 根据id名查找
print(soup.select('#link1')[0].text)
print(soup.select('a #link1'))
print(soup.select('a[class="sister"]')[0].text)
tag = soup.b
print(type(tag))
print(tag.parent['class'])

print(soup.head.contents)
for child in soup.children:
    print('child => ',child)