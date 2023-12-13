#!/bin/bash

# Check if a commit message is provided as an argument
if [ -z "$1" ]; then
  commit_message="submit"
else
  commit_message="$1"
fi

git add .
git commit -m "$commit_message"
git push
