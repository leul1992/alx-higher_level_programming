#!/usr/bin/python3
"""takes url and email, send post request to the url with the email
    and display the body of the response"""
if __name__ == '__main__':
    from sys import argv
    import urllib.request
    import urllib.parse

    url = argv[1]
    res = urllib.parse.urlencode({'email': argv[2]}).encode('ascii')
    with urllib.request.urlopen(url, res) as response:
        print(response.read().decode('utf-8'))
