"""
Task to find html links and their corresponding texts from raw html element string
"""

import re
import sys

regex_pattern = "\<a href=\"(?P<link_url>.*?)\".*?\>(?P<text>.*?)\<\/a"



t = int(sys.stdin.readline())
while t:

    raw_string = sys.stdin.readline()

    
    for match_obj in re.finditer(regex_pattern, raw_string):
        if match_obj:
            match_dict = match_obj.groupdict()
            link = match_dict['link_url'].strip()
            text = match_dict['text'].strip()
            print(f"{link},{text}")
    t -= 1

