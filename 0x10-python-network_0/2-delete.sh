#!/bin/bash
# Delete requests to the url passed as the first argument
curl -sX DELETE "$1"
