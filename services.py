#!/usr/bin/env python3

import servicesKeys
import urllib as ul
from urllib.error import HTTPError as hpe
import json
import os, sys, time
import requests

# Access token and API URL
parent_dir = '/home/pi/projects/Project3/'
web = 'https://vt.instructure.com/api/v1/courses/'
ckey = servicesKeys.ckey
course = '83639'
can_file = 'Assignment3.pdf'

# function to download file from canvas
payload = {'access_token' : ckey, 'search_term' : can_file}
r = requests.get(web+course+'/files', params = payload)
#url = web+course+'/files?search_term='+can_file+'&access_token='+ckey

try:
    # Fetch the course details
    can_file = ul.request.urlopen(r.url).read()

    # Parse the json response
    files = json.loads(can_file.decode('utf-8'))
    for file in files:
        # Deciding file location to save file
        file_loc = parent_dir
        print('file location:', file_loc)
        # Finding file url to download from
        file_url = file['url']
        print('url:', file_url)
        # Finding file to download from that url
        file_name = file['filename']
        print('filename:', file_name)
        file_path = file_loc + file_name
        # Downloading the file to the file location
        print('Downloading:', file_path)
        if not os.path.isfile(file_path):
            ul.request.urlretrieve(file_url, file_path)

except hpe as fileE:
    print('Error: No files with the given id')


