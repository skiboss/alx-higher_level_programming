#!/bin/bash
# Script that sends json POST req to URL
curl -sL -X POST -H "Content-Type: application/json" -d @"$2" "$1"
