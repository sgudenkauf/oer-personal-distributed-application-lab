#!/usr/bin/env python

import json
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == 'supports':
        # sys.argv[2] is the renderer name
        sys.exit(0)

# load book content
context, book = json.load(sys.stdin) 
# write back unmodified
json.dump(book, sys.stdout) 