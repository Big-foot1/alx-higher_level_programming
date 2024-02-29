#!/bin/bash
# display allowed http method 
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
