#!/bin/bash
#sends a request to url and display the size of the respose
curl -so /dev/null "$1" -w '%{size_download}\n'
