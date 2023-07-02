#!/bin/bash
# script sends a request to URL and displays the size of the response body
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
