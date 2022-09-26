#!/bin/bash
# display all http methods the server will accept
curl -s -I OPTIONS "$1" | grep "Allow" | cut -d " " -f2-
