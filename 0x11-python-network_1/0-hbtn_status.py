#!/usr/bin/python3
"""fetches url and display body of the response"""
if __name__ == '__main__':
    import urllib.request
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
