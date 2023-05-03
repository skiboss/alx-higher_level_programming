#!/bin/bash
# Script to set email and subject header variables
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
