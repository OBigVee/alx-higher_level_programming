#!/bin/bash
# script takes a url and send a 
# GET request to the URL and
# displays the body of the response
#curl -s -L "$1"

# Check if URL is provided as argument
if [ $# -eq 0 ]; then
  echo "Please provide a URL as an argument."
  exit 1
fi

# Send GET request and display the response body
response=$(curl -s -L "$1")
echo "$response"
