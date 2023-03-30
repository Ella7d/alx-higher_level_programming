#!/bin/bash
# Script that shows the content-Lenght from an HTTP request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
