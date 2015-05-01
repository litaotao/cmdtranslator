

import requests as r
from bs4 import BeautifulSoup as bs
import sys
from docopt import docopt


Models = {"iciba":["http://www.iciba.com/", "http://www.iciba.com/ajax_sugg.php?key="]}



def trans():
	'''
	translate the key. 
	'''
	# get the command arguments
	key = sys.argv[1]
	model = 'iciba'
	content = r.get(Models[model][0] + key)
	soup = bs(content.text)
	span = soup.findAll("span", {"class": "label_list"})
	real_word = soup.findAll("h1", {"id": "word_name_h1"})
	mean = []
	for i in span:
	    mean.extend(i.text.split('\n'))
	mean = [i for i in mean if i]

	# if key is a valid word
	if mean:
		word = real_word[0].text if real_word else key
		if word != key:
			print 'spell error ... \nreal:{}\nyour:{}\n'.format(word, key)
		for i in mean:
			print i
		return