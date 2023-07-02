#!/bin/bash

# Get the URL from the command line argument
url=$1

# Send a request to the URL and store the response in a variable
response=$(curl -s -X GET -I "$url")

# Extract the content length from the response headers
content_length=$(echo "$response" | grep -i -e "Content-Length" | awk '{print $2}' | tr -d '\r')

# Display the size of the response body in bytes
echo "$content_length"
