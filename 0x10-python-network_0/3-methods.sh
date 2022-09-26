#!/bin/bash
# display all http methods the server will accept
curl -i -s "$1" | grep 'Allow' | cut -c 8-
