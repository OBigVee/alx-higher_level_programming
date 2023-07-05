#!/bin/bash
# script takes in a URL as an argument, send a GET request to the URL and displays the body ofthe response curl --get -H "X-School-User-Id: 98" "$1"
curl -s -H "X-School-User-Id: 98" "$1"
