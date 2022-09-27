#!/bin/bash
# send POST request and display body of response
curl -X POST -d '"email": "test@gmail.com", "subject": "I will always be here for PLD"' -s "$1"
