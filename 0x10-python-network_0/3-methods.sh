#!/bin/bash
# display all http methods the server will accept
curl -i -L -X OPTIONS "$1" | grep 'Allow' | cut -d':' -f2 | sed 's/ //'
