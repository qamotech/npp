import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Found 'overflow-x: hidden' inside style:", len(re.findall(r'overflow-x:\s*hidden', content)))
print("Found 'overflow-wrap: break-word' inside style:", len(re.findall(r'overflow-wrap:\s*break-word', content)))
