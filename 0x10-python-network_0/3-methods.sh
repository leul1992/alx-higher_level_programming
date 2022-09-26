#!/bin/bash
# display all http methods the server will accept
curl -iLX OPTIONS.allow "$1"
