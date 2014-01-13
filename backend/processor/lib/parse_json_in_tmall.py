import re
import json

def parse_json(content):
    pn = re.compile(r'TShop.Setup\(([^\<\>\(\)]+)\);', re.M | re.S)
    m = pn.search(content)
    if not m:
        raise Exception('No match error')
    data = m.group(1)
    data = data.replace('\'', '"')
    replace_key_pn = r'(?<=[\s,\{])(\w+)\s*:\s*'
    data = re.sub(replace_key_pn, r'"\1":', data)
    return json.loads(data)

if __name__ == '__main__':
    print parse_json(open('tmall.html').read())
