import urllib.request
import re

html = urllib.request.urlopen('https://nalandaaquarium.com/blog.html').read().decode('utf-8')
srcs = re.findall(r'src="(.*?)"', html)
broken = []

print(f'Checking {len(srcs)} srcs')
for src in srcs:
    if src.startswith('http'):
        url = src
    else:
        url = 'https://nalandaaquarium.com/' + src
    
    url = url.replace(' ', '%20')
    
    try:
        req = urllib.request.Request(url, method='HEAD')
        urllib.request.urlopen(req)
    except Exception as e:
        broken.append((url, str(e)))

print('Broken:', broken)
