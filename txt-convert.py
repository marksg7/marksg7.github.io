import sys

assert len(sys.argv) >= 2

fname = sys.argv[1]
html = '''
<!DOCTYPE html>
<html>
<head>
'''
with open('script', 'r') as f:
	html += f.read()
html += '''
</head>
<body>'''
import chardet
ec = chardet.detect(open(fname, 'rb').read())['encoding']
with open(fname, 'r', encoding=ec) as f:
    for lin in f.readlines():
        html += f'<p>'
        html += lin.strip()
        html += '</p>'

html += '</body>'

with open('out.html', 'w', encoding='utf-8') as f:
    f.write(html)
#print(html)
