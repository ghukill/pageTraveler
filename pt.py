#!/usr/bin/env python

import requests
import json
import os
import sys

'''
To Add:
1) How many are there?
	- counter
	- decision making
2) Size arguments
'''

# get arguments here
'''coming soon...'''


if len(sys.argv) < 3:
	print "Not enough arguments found.  First arg should be site URL (http://www.foo.bar).  Second arg should be directory that is created in ./images folder for project."
	exit()
else:
	# get URL to crawl
	siteURL = sys.argv[1]
	projDir = sys.argv[2]

# create image directory
os.system("mkdir ./images/{projDir}".format(projDir=projDir))

# get list of LOCKSS page captures from archive.org
CDXqueryURL = "http://web.archive.org/cdx/search/cdx?url={siteURL}&output=json".format(siteURL=siteURL)
r = requests.get(CDXqueryURL)
# load as dict
capturesDict = json.loads(r.text)
# remove headers
capturesDict.pop(0)

print siteURL,"has",len(capturesDict),"captures."
# temporarily removed, hard to nohup with user input...
# choice = raw_input("Are you sure you want to continue (y/n)?  ")
# if choice != "y":
# 	exit()

# iterate through list, creating screenshots
for each in capturesDict:
	print "Capture date:",each[1],"/ HTTP response code:",each[4]
	
	# do check, if 302 code, skip row / dict entry
	if each[4] == "200":
		print "Content change for this crawl, grabbing image..."
		cmdString = "python python-webkit2png/scripts/webkit2png -x 1024 768 -o ./images/{projDir}/{captureDate}.png https://web.archive.org/web/{captureDate}/{siteURL}".format(captureDate=str(each[1]),projDir=projDir,siteURL=siteURL)
		print "Capturing:",cmdString
		os.system(cmdString)
		print "capture complete."
	else:
		print "Capture empty or HTTP 302 - unchanged content.  Moving on."

	# raw_input("shall we go on?") 

print "finis!"