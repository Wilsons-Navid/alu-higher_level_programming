#!/bin/bash
# Display all HTTP methods that can be accepted.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
