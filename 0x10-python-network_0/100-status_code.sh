#!/bin/bash
# Script to display status code of a HTTP response
curl -sw "%{http_code}" "$1" -o /dev/null
