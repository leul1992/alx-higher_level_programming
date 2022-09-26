#!/bin/bash
# display all http methods the server will accept
curl -i -H "Accept:" -X GET "$1"
