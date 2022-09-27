#!/bin/bash
#take url as arg, send GET request and display body of response
curl -sH "$1" -X GET "X-School-User-Id: 98"
