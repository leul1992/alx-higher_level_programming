#!/bin/bash
#take url as arg, send GET request and display body of response
curl -s "$1" -X GET -H "X-School-User-Id: 98"
