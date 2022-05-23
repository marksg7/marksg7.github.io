import sys

def stripEvil(s):
    i = 0
    fins = ''
    while s.find('《', i) != -1:
        st = s.find('《', i)
        e = s.find('》', st+1)
        assert e != -1 and 50 > e - st > 1, 'Gone wrong w evil stripping'
        fins += s[i:st]
        i = e + 1
    fins += s[i:]
    return fins

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

html = stripEvil(html)

with open('out.html', 'w', encoding='utf-8') as f:
    f.write(html)
#print(html)
