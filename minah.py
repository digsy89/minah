# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import explicit, relative
import re
import sys

def parse(sentence):
    result = explicit.parse(sentence)
    result += relative.parse(sentence)
    return result

if __name__ == "__main__":
    for text in sys.stdin:
        print "========================================="
        print text
        for k,v in parse(text):
            print k, v
