#!/usr/bin/env python

import requests
import json
import os

'''
To Add:
1) How many are there?
	- counter
	- decision making
2) Size arguments
'''

# get arguments here
'''coming soon...'''

# get list of LOCKSS page captures from archive.org
CDXqueryURL = "http://web.archive.org/cdx/search/cdx?url=http://www.lockss.org/&output=json"
r = requests.get(CDXqueryURL)
# load as dict
capturesDict = json.loads(r.text)
# remove headers
capturesDict.pop(0)

# iterate through list, creating screenshots
for each in capturesDict:
	# do check, if 302 code, skip row / dict entry
	cmdString = "python python-webkit2png/scripts/webkit2png -x 1024 768 -o /var/www/LOCKSS_screenshot_project/{captureDate}.png https://web.archive.org/web/{captureDate}/http://www.lockss.org/".format(captureDate=str(each[1]))
	print "Capturing:",cmdString
	os.system(cmdString)
	print "capture complete."
	# raw_input("shall we go on?") 

print "finis!"