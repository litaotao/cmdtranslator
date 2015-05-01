"""trans

Usage:
  trans word
  rodeo (-h | --help)

Options:
  -h --help     Show this screen.

Help:
Rodeo is a data centric IDE for python. It leverages the IPython
Kernel but presents a different user experience than the notebook. 
Those of you who use products like SublimeText or Eclipse will
probably find rodeo familiar.

Examples:
To run a rodeo server, just execute the `rodeo` command like so:
    $ trans <word> # basic usage

"""


import requests as r
from bs4 import BeautifulSoup as bs
import sys
from docopt import docopt


Models = {"iciba":["http://www.iciba.com/", "http://www.iciba.com/ajax_sugg.php?key="]}



def trans():
	'''
	translate the key. if key seems not a valid word, give some suggestions to the user.
	'''
	# get the command arguments
	# import pdb; pdb.set_trace()
	key = sys.argv[1]
	model = 'iciba'
	content = r.get(Models[model][0] + key)
	soup = bs(content.text)
	span = soup.findAll("span", {"class": "label_list"})
	mean = []
	for i in span:
	    mean.extend(i.text.split('\n'))
	mean = [i for i in mean if i]

	# if key is a valid word
	if mean:
		for i in mean:
			print i
		return 

	# if key isn't a valid word, give it some tips
	content = r.get(Models[model][1] + key)
	res = content.json()
	res = [i['key'] for i in res]
	for i in res:
		print i
	return 