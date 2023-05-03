#!/bin/bash
# Script that takes in a request, sends to a URl 
# and displays the content-length
curl -sI "$1" | grep 'Content-Length' | cut -d ' ' -f 2
