import requests
import sys
import json


def waybackurls(host, with_subs):
    if with_subs:
        url = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=json&fl=original&collapse=urlkey' % host
    else:
        url = 'http://web.archive.org/cdx/search/cdx?url=%s/*&output=json&fl=original&collapse=urlkey' % host
    r = requests.get(url)
    results = r.json()
    urls = results[1:]
    json_urls = json.dumps(urls)
    if urls:
        filename = '%s-waybackurls.json' % host
        with open(filename, 'w') as f:
            f.write(json_urls)
        print('[*] Saved results to %s' % filename)
    else:
        print('[-] Found nothing')