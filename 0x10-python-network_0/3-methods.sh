#!/bin/bash
# display all http methods the server will accept
curl -s -I "$1" | grep "Allow" | cut -d " " -f2-
