#!/bin/bash
# Takes in a URL...
curl -s -o /dev/null -w "%{http_code}" "$1"
