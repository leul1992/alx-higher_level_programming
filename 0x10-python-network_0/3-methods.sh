#!/bin/bash
# display all http methods the server will accept
curl -si -L -X OPTIONS "$1" | grep "Allow" | cut -d ":" -f2-
