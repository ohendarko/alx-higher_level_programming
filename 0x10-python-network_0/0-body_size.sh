#!/usr/bin/env bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response

url=$2

response_size=$(curl -sI "$url" | grep -i content-length | awk '{print $2}' | tr -d '\r')

echo $response_size