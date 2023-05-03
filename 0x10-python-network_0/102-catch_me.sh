#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a "You got me!" message in the response body
curl -s -X PUT -H 'Origin: HolbertonSchool' -L --max-redirs -1 -d "user_id=98" "0.0.0.0:5000/catch_me"
