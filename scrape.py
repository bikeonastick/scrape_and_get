#!/usr/bin/env python3
# -*- coding: UTF-8  -*-

from urllib.request import urlopen,urlretrieve
import optparse
import re
from urllib.parse import urlparse
import os
from shutil import rmtree
 
def main():
    p = optparse.OptionParser()
    p.add_option('--url', '-u', default="https://www.bikerumor.com")
    p.add_option('--directory', '-d', default="downloads")
    options, arguments = p.parse_args()

    create_save_directory(options.directory)
    with urlopen(options.url) as response:
        for line in response:
            images = get_image_uris_from_line(line.decode('utf-8'))
            for image in images:
                file_name = f"{options.directory}/{extract_filename(image)}"
                urlretrieve(image,file_name)

def create_save_directory(dir):
    if os.path.exists(dir):
        rmtree(dir, True)
    os.mkdir(dir)

def get_image_uris_from_line(line):
    pattern_to_find = r'''<img.*?src="(.*?)"'''
    return re.findall(pattern_to_find,line)

def extract_filename(uri):
    parsed = urlparse(uri)
    file_path = parsed.path
    if len(file_path) > 0:
        return file_path[(file_path.rfind('/')+1):len(file_path)]

if __name__ == '__main__':
    main()
