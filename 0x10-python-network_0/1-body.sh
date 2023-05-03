#!/bin/bash
# Script that takes and sends a GET to URL and displays body of response
curl -sb -X GET -L "$1"
