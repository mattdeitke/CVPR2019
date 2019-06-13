# From the CVPR website, this script will get the
# abstract for each paper.

import os
import requests

# get list of all PDFs supplied by CVPR
relpath = "content/"
allFiles = os.listdir(relpath)
paperids = [x[:-4] for x in allFiles if x.endswith(".pdf")]

# iterate over each paper
for i, pid in enumerate(paperids):
	# get the url to the page that contains the abstract
	url = 'http://openaccess.thecvf.com/content_CVPR_2019/html/' + pid + '.html'

	print("Processing:", pid, i, '/', len(paperids)) # monitor progress

	# get the abstract text from the html
	abstract = requests.get(url).text
	abstract = abstract[abstract.find('id="abstract"'):]
	abstract = abstract[abstract.find('>') + 1:abstract.find('</div')].strip()

	# checks for empty abstract
	# (often arises if link 404s)
	if (len(abstract) == 0):
		print('CHECK ABSTRACT FOR', pid)
		continue

	# create new .txt file in abstracts folder
	f = open("abstracts/" + pid + ".txt", "w")
	f.write(abstract)
	f.close()
