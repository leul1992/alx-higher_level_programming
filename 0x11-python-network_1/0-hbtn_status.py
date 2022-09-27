#!/usr/bin/python3
"""fetches url and display body of the response"""
if __name__ == '__main__':
    import urllib.request
    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        res = response.read()
        print("Body response:")
        print(f"\t- type: {type(res)}")
        print(f"\t- content: {res}")
        print(f"\t-utf8 content: {res.decode('utf8')}")
