# go over all pdfs and use imagemagick to convert 
# them all to a sequence of thumbnail images
# requires sudo apt-get install imagemagick
# or can be installed with brew install imagemagick

import os

relpath = "content/"
allFiles = os.listdir(relpath)
pdfs = [x for x in allFiles if x.endswith(".pdf")]

for i,f in enumerate(pdfs):
	paperid = f[:-20]
	fullpath = relpath + f

	print("processing %s, %d/%d" % (paperid[:5], i, len(pdfs)))

	# this is a mouthful... 
	# take first 8 pages of the pdf ([0-7]), since 9th page are references
	# tile them horizontally, use JPEG compression 80, trim the borders for each image
	# colorspace was added because a few PDFs displayed with a black background
	cmd = "montage %s[0-7] -mode Concatenate -colorspace sRGB -tile x1 -quality 80 -resize x345 -trim %s" % (fullpath, "thumbs/" + paperid + ".jpg")
	print("EXEC: " + cmd)
	os.system(cmd)


# an alternate, more roundabout alternative that is worse and requires temporary files, yuck!
#cmd = "convert -thumbnail x200 %s[0-7] test.png" % (fullpath, )
# os.system(cmd)
#cmd = "montage -mode concatenate -quality 80 -tile x1 test-*.png %s" % ("thumbs/" + f + ".jpg", )
# os.system(cmd)
