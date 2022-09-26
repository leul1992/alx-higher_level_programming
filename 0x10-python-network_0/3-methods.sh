#!/bin/bash
# display all http methods the server will accept
curl -iLX OPTIONS "$1" | grep Allow
