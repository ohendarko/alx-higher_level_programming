#!/bin/bash
# Takes in a URL...
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
