# scrape the cvpr2019oar.html file looking for authors names, titles, and bib
# and create a database of all papers. This is necessary because
# extracting the authors, titles, and bib from PDFs directly is tricky.

import pickle

# html = open('cvpr2019oar.html').read()
html = open('OAR2.html').read()
outdict = {}

while html.find('class="bibref"') != -1:
	# defining id as the pdf url to remain consistent with other sections
	# also removing '_CVPR_2019_paper.pdf' from each id
	paperid = html[:html.find('class="bibref"')]

	# checks for supplemental material
	# empty string if no supp, url to supp if there is supp
	supp = ''
	if 'supplemental' in paperid[paperid.rfind('paper.pdf'):]:
		supp = paperid[paperid.rfind('paper.pdf'):]
		supp = supp[supp.find('href'):]
		supp = supp[supp.find('"') + 1:supp.find('.pdf') + 4]

	paperid = paperid[:paperid.rfind('paper.pdf')]
	paperid = paperid[paperid.rfind('/')+1:-11]

	# used to get each of the titles and authors of the text
	bib = html[html.find('class="bibref"'):]
	bib = bib[bib.find('>') + 1:bib.find('</div>')].strip() \
												   .replace('\n', '\n&nbsp;&nbsp;') \
												   .replace('&nbsp;&nbsp;}', '}')

	# find the authors name and format with 'first last, first last, ...'
	authors = bib[bib.find('author'):]
	authors = authors[authors.find('{')+1:authors.find('}')].split(' and ')
	authors = ', '.join([n[n.find(', ')+2:] + ' ' + n[:n.find(',')] for n in authors])

	# title from bibtex
	title = bib[bib.find('title'):]
	title = title[title.find('{')+1:title.find('}')].strip()

	# save each entry into a dictionary
	outdict[paperid] = (title, authors, bib, supp)

	html = html[html.find('class="bibref"') + 1:]

# dump a dictionary indexed by paper id that points to (title, authors) tuple
pickle.dump(outdict, open("papers.p", "wb"))
