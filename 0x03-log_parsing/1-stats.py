#!/usr/bin/python3

import sys



print(sys.stdin)
for _ in sys.stdin:
    print(f"=> {_.split()},=>\n {len(_.split())}")
    if _ == '\n':
        print('THE END')