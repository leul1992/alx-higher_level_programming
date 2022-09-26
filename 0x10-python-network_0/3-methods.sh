#!/bin/bash
# display all http methods the server will accept
curl -s -i "$1" | grep "Allow" | cut -c 8-
