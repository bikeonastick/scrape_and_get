#!/usr/bin/env python3
# -*- coding: UTF-8  -*-

from urllib.request import urlopen
import optparse
import re
from urllib.parse import urlparse
 
def main():
    p = optparse.OptionParser()
    p.add_option('--url', '-u', default="https://www.bikerumor.com")
    p.add_option('--directory', '-d', default="downloads")
    options, arguments = p.parse_args()
    pattern_to_find = r'''<img.*?src="(.*?)"'''
    with urlopen(options.url) as response:
        for line in response:
            line = line.decode('utf-8')
            images = re.findall(pattern_to_find,line)
            for image in images:
                file_name = extract_filename(image)
                print(f' - {file_name}')
    #print(f'Hello {options.person}')

def extract_filename(uri):
    parsed = urlparse(uri)
    file_path = parsed.path
    if len(file_path) > 0:
        return file_path[(file_path.rfind('/')+1):len(file_path)]

if __name__ == '__main__':
    main()