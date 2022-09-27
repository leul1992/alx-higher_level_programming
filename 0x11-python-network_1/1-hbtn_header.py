#!/usr/bin/python3
""" takes url and sends request to url to display value
    of a variable found on the header"""
if __name__ == '__main__':
    import urllib.request
    from sys import argv

    url = argv[1]
    with urllib.request.urlopen(url) as response:
        res = response.info()

    print(res.get('X-Request-Id'))
