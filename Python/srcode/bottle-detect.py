# -*- coding: UTF-8 -*-

import json

import bottle
import requests

app = application = bottle.Bottle()

@app.route('/', method="GET")
def show_index():
    
    bottle.response.headers['accept-ch'] = "Sec-Ch-Ua,Sec-Ch-Ua-Full-Version,Sec-Ch-Ua-Platform,Sec-Ch-Ua-Platform-Version,Sec-Ch-Ua-Arch,Sec-Ch-Bitness,Sec-Ch-Ua-Model,Sec-Ch-Ua-Mobile,Device-Memory,Dpr,Viewport-Width,Downlink,Ect,Rtt,Save-Data,Sec-Ch-Prefers-Color-Scheme,Sec-Ch-Prefers-Reduced-Motion,Sec-Ch-Prefers-Contrast,Sec-Ch-Prefers-Reduced-Data,Sec-Ch-Forced-Colors"
    bottle.response.headers['critical-ch'] = "Sec-Ch-Ua,Sec-Ch-Ua-Full-Version,Sec-Ch-Ua-Platform,Sec-Ch-Ua-Platform-Version,Sec-Ch-Ua-Arch,Sec-Ch-Bitness,Sec-Ch-Ua-Model,Sec-Ch-Ua-Mobile,Device-Memory,Dpr,Viewport-Width,Downlink,Ect,Rtt,Save-Data,Sec-Ch-Prefers-Color-Scheme,Sec-Ch-Prefers-Reduced-Motion,Sec-Ch-Prefers-Contrast,Sec-Ch-Prefers-Reduced-Data,Sec-Ch-Forced-Colors"

    headers_to_send = []

    for header_name in bottle.request.headers:
        headers_to_send.append({
            "name": header_name,
            "value": bottle.request.headers.get(header_name),
        })

    #print(headers_to_send)

    headers = {
        'X-API-KEY': "YOURAPIKEYHERE",
    }
    post_data = {
        "headers": headers_to_send,
    }

    # -- make the request to the whatismybrowser server
    result = requests.post("https://api.whatismybrowser.com/api/v3/detect", data=json.dumps(post_data), headers=headers)

    #print(result.json())
    #print(result.json().get("detection").get("simple_software_string"))  # etc

    return "You are using %s" % result.json().get("detection").get("simple_software_string")


class StripPathMiddleware(object):
    '''Get that slash out of the request'''
    def __init__(self, a):
        self.a = a
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)

if __name__ == '__main__':
    bottle.run(app=StripPathMiddleware(app),
        host='0.0.0.0',
        port=6767)
