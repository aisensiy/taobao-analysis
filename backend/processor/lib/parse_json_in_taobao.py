import re
import json

def parse_json(content):
    pn = re.compile(r'g_config\.idata=(.+?)\}\)\(\);', re.MULTILINE)
    m = pn.search(content)
    if not m:
        return '{}'
    data = m.group(1)
    data = data.replace('\'', '"')
    replace_key_pn = r'(?<=[\s,\{])(\w+)\s*:\s*'
    data = re.sub(replace_key_pn, r'"\1":', data)
    return json.loads(data)

if __name__ == '__main__':
    print json.dumps(parse_json(open('tmall.html').read()))
