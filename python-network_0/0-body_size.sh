#!/bin/bash
# Get the byte size of http response
curl -s "$1" | wc -c
