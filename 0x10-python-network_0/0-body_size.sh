#!/bin/bash
# script sends a request to URL and displays the size of the response body

curl -s "$1" | wc -c
